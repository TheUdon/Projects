import pyautogui
from PIL import Image
from datetime import datetime, timedelta
import time as t
import os

# I have 2 monitors so there are some negative values
# Functions for automation
def go_to_email():
    pyautogui.hotkey("ctrl", "t")
    pyautogui.typewrite("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    pyautogui.press("enter")


def close_extra_window():
    pyautogui.click(619, 1422)
    t.sleep(2)
    pyautogui.click(591, 1260)


def get_old_tabs():
    pyautogui.hotkey("ctrl", "shift", "t")
    t.sleep(2)
    go_to_email()
    pyautogui.click(500,500)
    t.sleep(1)
    close_extra_window()
    pyautogui.click(500, 500)



screen = pyautogui
# Get Icon img files
chrome_im = pyautogui.screenshot(region=(0, 800, 70, 90))
if os.path.exists("C:/Users/dsk99/PycharmProjects/automate_computer_startup/chrome.png"):
    pass
else:
    chrome_im.save("chrome.png")
discord_im = pyautogui.screenshot(region=(300, 0, 70, 70))
if os.path.exists("C:/Users/dsk99/PycharmProjects/automate_computer_startup/discord.png"):
    pass
else:
    discord_im.save("discord.png")

# Automation starts
chrome = pyautogui.locateOnScreen('chrome.png')
chrome_center = pyautogui.center(chrome)
pyautogui.doubleClick(chrome_center.x, chrome_center.y)
t.sleep(2)
pyautogui.click(-400, 200)
get_old_tabs()
discord = pyautogui.locateOnScreen('discord.png')
discord_center = pyautogui.center(discord)
pyautogui.doubleClick(discord_center.x, discord_center.y)

# Code for finding mouse position on screen.
# program_on = True
#
# time = datetime.now()
# time_limit = time + timedelta(minutes=30)
#
# while program_on:
#     current_time = datetime.now()
#     second = datetime.now().second
#     print(pyautogui.position())
#     if current_time > time_limit:
#         game_on = False
