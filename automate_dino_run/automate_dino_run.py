import pyautogui
from PIL import Image
from selenium import webdriver
from datetime import datetime, timedelta
import time as t
import os

# Code works, but need to fine tune when to jump
# Setting up Chrome Driver
chrome_driver_path = "/Users/dsk99/OneDrive/Documents/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://elgoog.im/t-rex/")

t.sleep(1)
screen = pyautogui
trex_im = pyautogui.screenshot(region=(975, 410, 50, 50))
if os.path.exists("C:/Users/dsk99/PycharmProjects/automate_dino_run/trex.png"):
    pass
else:
    trex_im.save("trex.png")
trex = pyautogui.locateOnScreen('trex.png')
t.sleep(1)
pyautogui.press("up")
game_on = True

# Functions for trex
def jump_over_obstable():
    pyautogui.press("up")

def jump_over_obstable_fast():
    pyautogui.keyDown("down")
    t.sleep(0.5)
    pyautogui.keyUp("down")

def check_for_obstacle(jumps):
    if pyautogui.pixelMatchesColor(1070 + jumps, 435, trex_im.getpixel((25, 25))) and pyautogui.pixelMatchesColor(1105 + jumps, 435, trex_im.getpixel((25, 25))) and pyautogui.pixelMatchesColor(1140 + jumps, 435, trex_im.getpixel((25, 25))):
        jump_over_obstable_fast()
    elif pyautogui.pixelMatchesColor(1090 + jumps, 435, trex_im.getpixel((25, 25))) and (pyautogui.pixelMatchesColor(1130 + jumps, 435, trex_im.getpixel((25, 25))) or pyautogui.pixelMatchesColor(1180 + jumps, 435, trex_im.getpixel((25, 25)))):
        jump_over_obstable_fast()
    elif pyautogui.pixelMatchesColor(1070 + jumps, 435, trex_im.getpixel((25, 25))):
        jump_over_obstable()
    else:
        pass

time = datetime.now()
time_limit = time + timedelta(minutes=30)

while game_on:
    current_time = datetime.now()
    second = datetime.now().second
    jumps = 0

    check_for_obstacle(jumps)
    if current_time > time_limit:
        game_on = False

# driver.quit()