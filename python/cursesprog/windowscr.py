#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals, annotations)
import curses


def main():

    # The `screen` is a window that acts as the master window
    # that takes up the whole screen. Other windows created
    # later will get painted on to the `screen` window.
    screen = curses.initscr()

    # lines, columns, start line, start column
    my_window = curses.newwin(15, 20, 0, 0)

    # Long strings will wrap to the next line automatically
    # to stay within the window
    my_window.addstr(4, 4, "Hello from 4,4")
    my_window.addstr(5, 15, "Hello from 5,15 with a long string")
    my_window.border()

    # Print the window to the screen
    my_window.refresh()
    curses.napms(2000)

    # Clear the screen, clearing my_window contents that were printed to screen
    # my_window will retain its contents until my_window.clear() is called.
    screen.clear()
    screen.refresh()

    # Move the window and put it back on screen
    # If we didn't clear the screen before doing this,
    # the original window contents would remain on the screen
    # and we would see the window text twice.
    my_window.mvwin(10, 10)
    my_window.refresh()
    curses.napms(1000)

    # Clear the window and redraw over the current window space
    # This does not require clearing the whole screen, because the window
    # has not moved position.
    my_window.clear()
    my_window.refresh()
    curses.napms(1000)

    curses.endwin()


if __name__ == '__main__':
    main()
