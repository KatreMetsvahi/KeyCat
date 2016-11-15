# KeyCat

## Overview
KeyCat is a program that works in the background, analyzing the user's keyboard and mouse actions. When KeyCat detects a mouse action that can also be performed with a keyboard, it shows a notification in the corner of the screen. A keyboard shortcut that can be used to achieve the same result is displayed in that notification. The notification will fade away on its own in order not to disrupt the normal workflow of the user. Over time the user will start remembering more shortcuts and become more proficient in using their keyboard.

KeyCat holds a list of program specific shortcuts, which can also be customized according to users' needs.

Users can also view statistics on their keyboard and mouse usage, which will give them an overview of their progress and encourage further improvements.

Although these kind of programs already exist, there are currently no programs like this for Linux, which is what we are going to change. Examples of currently existing programs: KeyRocket (Windows), AltMOUSE (Windows), Hotkey EVE (Mac), KeyCue (Mac).

## Cloning
To clone this repository run
~~~
git clone <url>
~~~

## Updating
To pull the changes in this repository run
~~~
git pull
~~~

## Installing dependencies
To install necessary packages on Linux run with root permissions
~~~
./setup.sh
~~~

## Building
To build project run
~~~~
python setup.py install
~~~~

## Run
~~~~
python keycat
~~~~

## Close
~~~~
ctrl + z
~~~~

## Running tests
TBA