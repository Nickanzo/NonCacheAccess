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
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from dbCon import retrieve_pwd, customDecrypt
import settings

def open_ifc(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.NAME, value='user.login').send_keys(usr)
    browser.find_element(by=By.NAME, value='user.senha').send_keys(pwd)
    browser.find_element(by=By.NAME, value='user.senha').submit()

def open_linkedin(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.ID, value='username').send_keys(usr)
    browser.find_element(by=By.ID, value='password').send_keys(pwd)
    browser.find_element(by=By.ID, value='password').submit()
    #browser.find_element(by=By.CLASS_NAME, value='btn__primary--large from__button--floating').click()

def open_google(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.ID, value='identifierId').send_keys(usr)
    browser.find_element(by=By.ID, value='identifierNext').click()

    time.sleep(5)

    browser.find_element(by=By.NAME, value='Passwd').send_keys(pwd)
    browser.find_element(by=By.ID, value='passwordNext').click()


def open_amazon(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.ID, value='ap_email').send_keys(usr)
    browser.find_element(by=By.ID, value='continue').click()

    time.sleep(5)

    browser.find_element(by=By.NAME, value='ap_password').send_keys(pwd)
    browser.find_element(by=By.ID, value='signInSubmit').click()


def open_facebook(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)


def open_netflix(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)


def access_account(username, password, url, web):

    PATH = "..\\webDrivers\\Edge\\msedgedriver.exe"

    service = Service(PATH)

    pwd = retrieve_pwd(username,web)

    decrypted = customDecrypt(pwd[0], password)

    match web:
        case 'LinkedIn':
            open_linkedin(service, url, username, decrypted)
        case 'Google':
            open_google(service, url, username, decrypted)
        case 'IFC':
            open_ifc(service, url, username, decrypted)
        case 'Amazon':
            open_amazon(service, url, username, decrypted)
