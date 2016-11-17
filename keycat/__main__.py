import sys
from mouse_events import FullscreenMouseEventCreator, MouseEventListener, MouseClickEventListener, \
    FixedSizeScreenshotEventCreator
from events import EventReceiver
from screen import ScreenshotTaker, ScreenManager
from keyboard_events import KeyboardEventListener, KeyboardListener, KeyboardStateManager
from keycat.repository import ButtonRepository
from button_matcher import ButtonMatcher
from template_matcher import CCOEFFNORMEDTemplateMatcher
from keycat.database import *
from keycat.program_identifier import *
from time import sleep
import signal


def exit_program(signal, frame):
    print('Keycat terminated!')
    sys.exit(0)

def main():
    session = get_database_scoped_session()
    button_repository = ButtonRepository(session)
    load_data_to_database(button_repository)

    program_identifier = ProgramIdentifier()
    button_matcher = ButtonMatcher(CCOEFFNORMEDTemplateMatcher(), button_repository)

    event_receiver = EventReceiver(button_matcher)

    keyboard_event_listener = KeyboardEventListener(KeyboardListener(
        KeyboardStateManager(event_receiver, program_identifier)))
    keyboard_event_listener.daemon = True
    keyboard_event_listener.start()

    mouse_event_creator = FixedSizeScreenshotEventCreator(ScreenshotTaker(), ScreenManager(), program_identifier,
                                                          700, 100)

    mouse_click_listener = MouseClickEventListener(
        MouseEventListener(mouse_event_creator, event_receiver))
    mouse_click_listener.daemon = True
    mouse_click_listener.start()

    while 1:
        signal.signal(signal.SIGINT, exit_program)
        sleep(1)



if __name__ == '__main__':
    sys.exit(main())
