#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 07/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" App GUI """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import tkinter
from settings import MAIN_SIZE


# Window default constructor
def create():
    # Main window
    main = tkinter.Tk()
    # Set main window size
    set_size(main, MAIN_SIZE)
    # Return the new window
    return main


# Window parametrized constructor
def create(size, title):
    # Main window
    main = tkinter.Tk()
    # Set main window size
    set_size(main, size)
    # Set main window title
    set_title(main, title)
    # Return the new window
    return main


# Change window size
def set_size(window, size):
    window.geometry(size)


def set_title(window, text):
    window.title(text)
