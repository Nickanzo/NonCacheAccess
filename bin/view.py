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


# Window initialization
def create():
    # Main window
    main = tkinter.Tk()
    # Set main window size
    size(main, MAIN_SIZE)
    # Return the new window
    return main


# Change window size
def size(window, size):
    window.geometry(size)


def title(window, text):
    window.title(text)
