#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 07/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Window related tests """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from bin.view import *

# 1st Screen definition
def screen_1():


# 2nd Screen definition
def screen_2():


# Screen invoker
def call_scr(scr_num):
    match scr_num:
        case 1:
            screen_1()
        case 2:
            screen_2()
        case _:
          print('Fail to load Screen')

# Check Screen Input
def check_input():
    if text_input1.get():
        msg['text'] = 'Input has been submitted'
        text_input1.delete(0, len(text_input1.get()))
        return True
    else:
        msg['text'] = 'Input is empty'

    return False


# Action listener for Window
def action(b):
    match b:
        case 1:
            print('Button 1 was pressed')
        case 2:
            print('Button 2 was pressed')
        case 3:
            print('Button 3 was pressed')
        case 4:
            check_input()
        case _:
            print('A button was pressed')


if __name__ == '__main__':

    # |✓| 1st Test, create window
    app = create()

    # |✓| 2nd Test, add Text
    title = tkinter.Label(app, text='Window Test')
    title.pack()

    # |✓| 3rd Test, create inputs
    text_input1 = tkinter.Entry(app)
    text_input2 = tkinter.Entry(app)
    text_input1.pack()
    text_input2.pack()

    # |✓| 4th Test, create buttons
    button1 = tkinter.Button(app, text='1st Test Button', padx=30, pady=1, command=lambda: action(1))
    button2 = tkinter.Button(app, text='2nd Test Button', padx=30, pady=1, command=lambda: action(2))
    button3 = tkinter.Button(app, text='3rd Test Button', padx=30, pady=1, command=lambda: action(3))
    button1.pack()
    button2.pack()
    button3.pack()

    # |✓| 5th Test, use methods for field validation
    button4 = tkinter.Button(app, text='Submit', padx=30, pady=1, command=lambda: action(4), bg='white')
    button4.pack()
    msg = tkinter.Label(app)
    msg.pack()


    # | | 6th Test, call 2nd Screen
    call_scr(2)

    # | | 7th Test, return to 1st Screen

    app.mainloop()
