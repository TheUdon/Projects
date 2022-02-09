from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

gatcha_mode = input("Do you want gatcha mode? Y or N\n")
chrome_driver_path = "/Users/dsk99/OneDrive/Documents/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login.click()
time.sleep(1)

facebook_login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]")
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
accept = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/button")
accept.click()

driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys("dsk.9996@yahoo.com")
password = driver.find_element(By.ID, "pass")
password.send_keys("$up3rSonicDash9012")
login_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
login_button.click()
time.sleep(5)

driver.switch_to.window(base_window)

enable = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
enable.click()

location = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
location.click()
time.sleep(8)
like = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")
dislike = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
bot_on = True
while bot_on:
    try:
        if gatcha_mode.capitalize() == "Y":
            gatcha = randint(1, 10)
            if gatcha <= 5:
                time.sleep(2)
                dislike.click()
            elif gatcha > 5:
                time.sleep(2)
                like.click()
        else:
            time.sleep(2)
            like.click()
    except ElementClickInterceptedException:
        x_button = driver.find_element(By.XPATH, '//*[@id="q-818258919"]/div/div/div[1]/div/div[4]/button/svg/path')
        x_button.click()
        continue
    except NoSuchElementException:
        time.sleep(3)
        not_interested = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/button[2]")
        not_interested.click()
        continue