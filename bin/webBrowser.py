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
from dbCon import load_websites
import settings

def open_linkedin(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.ID, value='email').send_keys(usr)
    browser.find_element(by=By.ID, value='password').send_keys(pwd)
    browser.find_element(by=BY, value='js_btn_login').click()

def open_google(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

    browser.get(url)
    browser.find_element(by=By.ID, value='identifierId').send_keys(usr)
    browser.find_element(by=By.ID, value='identifierNext').click()

    time.sleep(2)

    browser.find_element(by=By.NAME, value='Passwd').send_keys(pwd)
    browser.find_element(by=By.ID, value='passwordNext').click()



def open_facebook(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

def open_netflix(srv, url, usr, pwd):
    browser = webdriver.Edge(service=srv)

def access_account(username, password, url, web):

    PATH = "..\\webDrivers\\Edge\\msedgedriver.exe"

    service = Service(PATH)

    match web:
        case 'LinkedIn':
            open_linkedin(service, url, username, password)
        case 'Google':
            open_google(service, url, username, password)
