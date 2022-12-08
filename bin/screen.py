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
import customtkinter
import tkinter

from bin.dbCon import retrieve_account, create_user, retrieve_con, encryptPass, create_account, load_websites
from bin.view import *
from bin.login import login
from bin.user import load_user
from tkinter import *
from bin.webBrowser import access_account
import settings
import tkinter.ttk as ttk


# Screen values validation
def check_login(username, password):
    # if username and password:
    if not login(username, password):
        messagebox.showerror('Login failed!')


def open_link(tree):

    selected = tree.focus()

    sel_account = tree.item(selected)

    website = sel_account.get("text")

    web_account = retrieve_account(retrieve_con(), website)

    access_account(web_account[0], web_account[1], web_account[2], web_account[3])

def delete_account(tree):

    selected = tree.focus()

    sel_account = tree.item(selected)

    answer = messagebox.askyesno(title="Delete",
                                 message="Do you want to delete this account?")

    if answer:
        tree.delete(sel_account)

    tree.update()

    #item = sel_account.get("text")



def create_tree(scr, data, con):
    tv = ttk.Treeview(scr, column=("c1"),show='tree')

    ybar = ttk.Scrollbar(scr, orient=tkinter.VERTICAL,
                         command=tv.yview)

    tv.configure(yscroll=ybar.set)
    tv.heading('#0', text='Contas')

    website = load_websites(retrieve_con())

    for i, accounts in enumerate(data):
        if accounts in website:
            parent = i
            tv.insert('', tkinter.END, text=accounts, iid=i)
        else:
            tv.insert(parent, tkinter.END, text=accounts, iid=i)
            tv.bind('<Double-Button-1>', lambda event: open_link(tv))
            tv.bind('<Button-3>', lambda event: delete_account(tv))

    tv.column("#1", width=150)
    tv.grid(row=0, column=0, padx=20, pady=25)


def new_scr(name):
    # Create new Screen
    scr = customtkinter.CTk()
    # Size
    match name:
        case 'login':
            scr.geometry("920x520")
        case 'user':
            scr.geometry("1080x450")
    # App Title
    scr.title("NonCacheAccess")
    scr.iconbitmap(default="..\\img\\icon.ico")
    scr.title("NonCache Access")

    return scr


def new_frame(scr):
    # Frame
    frame = customtkinter.CTkFrame(master=scr)
    frame.pack(pady=25, padx=25, fill="both", expand=True)

    return frame


def grid_frame(scr, row, col):
    # Frame
    frame = customtkinter.CTkFrame(master=scr)
    frame.grid(row=row, column=col, padx=50, pady=20)

    return frame


def new_tab(scr, width, height):
    # Create Tkinter Tab
    tabview = customtkinter.CTkTabview(master=scr, width=width, height=height)
    return tabview


def user_scr(con, username):
    main_scr = new_scr("user")

    def user_create_account(accountLogin, accountPwd, accountName, accountURL):

        con = retrieve_con()

        if con.is_connected():
            if accountURL == 'Website':
                addMsg.configure(text="Select a Website!")
            elif len(accountLogin) == 0 or len(accountPwd) == 0 or len(accountName) == 0:
                addMsg.configure(text="Fill all the Fields!")
            elif create_account(con, settings.__user__, accountLogin, accountPwd, accountName, accountURL):
                addMsg.configure(text="Account created!")
                main_scr.destroy()
                user_scr(retrieve_con(), username)
            else:
                addMsg.configure(text="Account couldn't be created!")

    def user_logoff():
        main_scr.destroy()
        settings.__user__ = ''
        login_scr()

    welcomeText = "Welcome back, " + settings.__user__

    # Title
    labelTitle = customtkinter.CTkLabel(master=main_scr, text=welcomeText, justify=tkinter.LEFT,
                                        font=customtkinter.CTkFont(size=20))
    labelTitle.pack(side=tkinter.TOP, anchor='w', pady=(15,0), padx=25)

    tab = new_tab(main_scr, 1000, 350)
    tab.add("Accounts")
    tab.grid_columnconfigure((0, 1), weight=1)
    tab.pack(padx=25, pady=10)

    ###############
    # Accounts  ###
    ###############

    usr_acc = load_user(con, username)
    if len(usr_acc) > 0:
        frame = grid_frame(customtkinter.CTkTabview.tab(tab, "Accounts"), 0, 0)
        create_tree(frame, usr_acc, con)

    ###################
    # Add Account   ###
    ###################

    accountName = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tab, "Accounts"),
                                         placeholder_text="Account Name", width=250,
                                         font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    accountName.grid(row=0, column=1, padx=100, pady=(0, 200), sticky="ew")
    accountName.focus_force()

    websites = load_websites(retrieve_con())
    domain = StringVar(customtkinter.CTkTabview.tab(tab, "Accounts"))

    website = customtkinter.CTkOptionMenu(master=customtkinter.CTkTabview.tab(tab, 'Accounts'),
                                          values=websites, variable=domain)
    website.grid(row=0, column=1, padx=100, pady=(0, 100), sticky="ew")
    website.set("Website")

    accountLogin = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tab, "Accounts"),
                                          placeholder_text="Login", width=250,
                                          font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    accountLogin.grid(row=0, column=1, padx=100, pady=(0, 0), sticky="ew")

    accountPwd = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tab, "Accounts"),
                                        placeholder_text="Password", width=250,
                                        font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    accountPwd.configure(show='*')
    accountPwd.grid(row=0, column=1, padx=100, pady=(100, 0), sticky="ew")

    addButton = customtkinter.CTkButton(master=customtkinter.CTkTabview.tab(tab, "Accounts"),
                                        command=lambda: user_create_account(accountLogin.get(), accountPwd.get(),
                                                                            accountName.get(), website.get()),
                                        text="Add Account",
                                        font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    addButton.grid(row=0, column=1, padx=100, pady=(225, 0))

    addMsg = customtkinter.CTkLabel(master=customtkinter.CTkTabview.tab(tab, "Accounts"),
                                    justify=tkinter.CENTER, text='')
    addMsg.grid(row=0, column=1, padx=100, pady=(155, 0))

    # Logoff Button
    logoff = customtkinter.CTkButton(master=main_scr, text="Log off", command=user_logoff, width=25, height=25)
    logoff.pack(side=tkinter.TOP, anchor="e", padx=25, pady=5)

    main_scr.mainloop()


# Screen initialization
def login_scr():
    scr_login = new_scr("login")

    def user_login(username, password):
        if username and password:
            con = login(username, password)
            if not con.is_connected():
                loginMsg.configure(text='Incorrect username or password!')
            else:
                scr_login.destroy()
                user_scr(con, username)
        else:
            loginMsg.configure(text='Fill all fields!')

    def user_signin(newUser, newPass, newPass2):
        if newUser and newPass and newPass2:
            if newPass2 != newPass:
                registerMsg.configure(text="Password doesn't match!")
            else:
                password = encryptPass(newPass)
                if bool(create_user(retrieve_con(), newUser, password)):
                    registerMsg.configure(text='User created!')
                else:
                    registerMsg.configure(text='Error!')
        else:
            registerMsg.configure(text='Fill all fields!')

    def toggleTheme():
        if not customtkinter.get_appearance_mode() == "Dark":
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")

    frame = new_frame(scr_login)

    # Title
    labelTitle = customtkinter.CTkLabel(text='NonCacheAccess', master=frame, justify=tkinter.LEFT,
                                        font=customtkinter.CTkFont(size=35, weight="bold"))
    labelTitle.pack(pady=45, padx=10)

    # Login/Register Tab
    tabview = new_tab(frame, 200, 70)
    tabview.pack(pady=0, padx=10)
    tabview.add("Login")
    tabview.add("Register")

    ###############
    # LOGIN TAB ###
    ###############

    userLogin = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview, "Login"),
                                        placeholder_text="Username", width=250,
                                        font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    userLogin.grid(row=0, column=0, padx=20, pady=(20, 10))


    passwordLogin = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview, "Login"),
                                           placeholder_text="Password", width=250,
                                           font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    passwordLogin.configure(show='*')
    passwordLogin.grid(row=1, column=0, padx=20, pady=(20, 10))

    loginButton = customtkinter.CTkButton(master=customtkinter.CTkTabview.tab(tabview, "Login"),
                                          command=lambda: user_login(userLogin.get(), passwordLogin.get()),
                                          text="Login",
                                          font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    loginButton.grid(row=3, column=0, padx=20, pady=8)

    # Error Message
    loginMsg = customtkinter.CTkLabel(master=customtkinter.CTkTabview.tab(tabview, "Login"),
                                      justify=tkinter.CENTER, text='')
    loginMsg.grid(row=2, column=0, padx=20, pady=0)

    ###################
    # REGISTER TAB  ###
    ###################

    userRegister = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview, "Register"),
                                          placeholder_text="New Username", width=250,
                                          font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    userRegister.grid(row=0, column=0, padx=20, pady=(20, 10))

    passRegister = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview, "Register"),
                                          placeholder_text="New Password", width=250,
                                          font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    passRegister.configure(show='*')
    passRegister.grid(row=1, column=0, padx=20, pady=(20, 10))

    passConfirm = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview, "Register"),
                                         placeholder_text="Confirm Password", width=250,
                                         font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    passConfirm.configure(show='*')
    passConfirm.grid(row=2, column=0, padx=20, pady=(20, 10))

    registerButton = customtkinter.CTkButton(master=customtkinter.CTkTabview.tab(tabview, "Register"),
                                             command=lambda: user_signin(userRegister.get(), passRegister.get(),
                                                                         passConfirm.get()),
                                             text="Register",
                                             font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
    registerButton.grid(row=4, column=0, padx=20, pady=8)

    registerMsg = customtkinter.CTkLabel(master=customtkinter.CTkTabview.tab(tabview, "Register"),
                                         justify=tkinter.CENTER, text='')
    registerMsg.grid(row=3, column=0, padx=20, pady=0)

    # GUI Theme Switch
    switchTheme = customtkinter.CTkSwitch(master=frame, text='', command=lambda: toggleTheme())
    switchTheme.pack(side=tkinter.BOTTOM, anchor="e", padx=0, pady=8)

    tabview.focus_force()

    scr_login.mainloop()

