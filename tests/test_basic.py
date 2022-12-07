#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Nicolas Escobar
# Created Date: 17/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Database related tests """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from bin.dbCon import create_account, delete_account, load_accounts  # DB connection
from bin.login import login
import settings  # App Global info

import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1100x580")
app.title("NonCacheAccess")


def button_callback():
    print("Button click", combobox_1.get())


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=25, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text='NonCacheAccess', master=frame_1, justify=tkinter.LEFT,
                                 font=customtkinter.CTkFont(size=35, weight="bold"))
label_1.pack(pady=45, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Username", width=250,
                                 font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Password", width=250,
                                 font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
entry_2.configure(show='*')
entry_2.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Login",
                                   font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
button_1.pack(pady=25, padx=10)



optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.pack(side=tkinter.BOTTOM, anchor="e", padx=8, pady=8)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = customtkinter.CTkTabview(master=frame_1, width=200, height=70)
tabview_1.pack(pady=0, padx=10)
tabview_1.add("Login")
tabview_1.add("Register")

entry_3 = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview_1, "Login"), placeholder_text="Username",
                                 width=250, font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
entry_3.grid(row=0, column=0, padx=20, pady=(20, 10))

entry_4 = customtkinter.CTkEntry(master=customtkinter.CTkTabview.tab(tabview_1, "Login"), placeholder_text="Password",
                                 width=250, font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
entry_4.configure(show='*')
entry_4.grid(row=1, column=0, padx=20, pady=(20, 10))

button_2 = customtkinter.CTkButton(master=customtkinter.CTkTabview.tab(tabview_1, "Login"), command=button_callback,
                                   text="Login", font=customtkinter.CTkFont(size=16, weight="bold", family="Arial"))
button_2.grid(row=2, column=0, padx=20, pady=(20, 10))

app.mainloop()

# ---------------------------------------------------------------------------
# if __name__ == '__main__':
#
#     # |✓| 1st Test, Log In
#     logged = login('p3pito', 'pepo123')
#     print(logged.is_connected())
#
#     # |✓| 2nd Test, Create Accounts
#     if login:
#         print(create_account(logged, settings.__user__, 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))
#         print(create_account(logged, settings.__user__, 'pepo2@email.com', 'pepo1234', 'EmailPepito2', 'www.gmail.com'))
#         print(create_account(logged, settings.__user__, 'pepo3@email.com', 'pepo1235', 'EmailPepito3', 'www.gmail.com'))
#         print(create_account(logged, settings.__user__, 'pepo4@email.com', 'pepo1236', 'EmailPepito4', 'www.gmail.com'))
#         print(create_account(logged, settings.__user__, 'pepo5@email.com', 'pepo1237', 'EmailPepito5', 'www.gmail.com'))
#         print(create_account(logged, settings.__user__, 'pepo@domain.com', 'pepodom', 'DomPepito', 'www.pepito.com'))
#
#     # |✓| 3rd Test, Don't allow create Account for different Login
#         print(create_account(logged, 'pepita', 'pepa@email.com', 'pepa123', 'EmailPepita', 'www.gmail.com'))
#         print(create_account(logged, 'pepito', 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))
#
#     # |✓| 4th Test, Don't allow create same Account twice
#         print(create_account(logged, settings.__user__, 'pepo@email.com', 'pepo123', 'EmailPepito', 'www.gmail.com'))
#
#     # |✓| 5th Test, Delete Accounts
#         print(delete_account(logged, settings.__user__, 'pepo@email.com', 'www.gmail.com'))
#
#     # |✓| 6th Test, Only Delete Existing Accounts
#         print(delete_account(logged, 'pepita', 'pepa@email.com', 'www.gmail.com'))
#
#     # |✓| 7th Test, Load Accounts
#         print(load_accounts(logged, settings.__user__))
