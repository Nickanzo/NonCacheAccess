#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 12/09/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Login Screen """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from tkinter import messagebox

from bin.dbCon import retrieve_account
from bin.view import *
from bin.login import login
from bin.user import load_user
from tkinter import *
import tkinter.ttk as ttk


# Screen values validation
def check_login(username, password):
    # if username and password:
    if not login(username, password):
        messagebox.showerror('Login failed!')


def open_link(account, con):

    account = retrieve_account(con, account)

    for accounts in account:
        site_login = accounts[0]
        site_pass = accounts[1]
        site_url = accounts[2]

    


def create_tree(scr, data, con):

    tv = ttk.Treeview(scr, show='tree')

    ybar = ttk.Scrollbar(scr, orient=tkinter.VERTICAL,
                        command=tv.yview)

    #tv.configure(yscroll=ybar.set)
    tv.heading('#0', text='Contas')

    for i, accounts in enumerate(data):
        if accounts.__contains__("www."):
            parent = i
            tv.insert('', tkinter.END, text=accounts, iid=i)
        else:
            tv.insert(parent, tkinter.END, text=accounts, iid=i)
            tv.bind('<Double-Button-1>', lambda event: open_link(accounts, con))

        tv.pack()


def user_scr(con, username):
    main_scr = Tk()
    main_scr.minsize(height=300, width=600)

    def user_logoff():
        main_scr.destroy()
        login_scr()

    #main_scr.title(text='Welcome ' + username)
    # scr_title.config(text='Welcome ' + username)

    usr_acc = load_user(con, username)
    if len(usr_acc) > 0:
        create_tree(main_scr, usr_acc, con)

    user_back = tkinter.Button(main_scr, text='Back', command=user_logoff)
    user_back.pack()


# Screen initialization
def login_scr():
    scr_login = Tk()
    scr_login.minsize(height=300, width=600)

    def user_login(username, password):
        if username and password:
            con = login(username, password)
            if not con.is_connected():
                msg_err['text'] = 'Login Failed!'
            else:
                scr_login.destroy()
                user_scr(con, username)
        else:
            msg_err['text'] = 'Fill all fields!'
    # Title
    scr_title = tkinter.Label(scr_login, text='Login', font='Futura 14')
    scr_title.pack()
    # Username
    scr_user = tkinter.Entry(scr_login)
    scr_user.pack()
    # Password
    scr_pass = tkinter.Entry(scr_login, show='*', width=15)
    scr_pass.pack()
    # Login Button
    scr_login_but = tkinter.Button(scr_login, text='Login', command=lambda: user_login(scr_user.get(), scr_pass.get()))
    scr_login_but.pack()
    # Error Message
    msg_err = tkinter.Label(scr_login)
    msg_err.pack()

    scr_login.mainloop()
