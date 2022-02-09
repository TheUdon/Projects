from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time

chrome_driver_path = "/Users/dsk99/OneDrive/Documents/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_tab = driver.current_window_handle
print(cookie_tab)
time.sleep(2)
driver.execute_script('''window.open("https://www.youtube.com/watch?v=Ut8MCXYOgNk");''')
all_tabs = driver.window_handles
print(all_tabs)
driver.switch_to.window(all_tabs[1])
print(driver.current_window_handle)
time.sleep(2)
driver.switch_to.window(cookie_tab)
time.sleep(1)
print(cookie_tab)

cookie = driver.find_element(By.CSS_SELECTOR, "#game #bigCookie")
game_on = True

def buy_upgrade():
    for i in range(0, 18):
        try:
            product = driver.find_element(By.ID, f"upgrade{i}")
            product.click()
        except IndexError:
            pass
        except:
            pass


def buy_item():
    for i in range(16, -1, -1):
        try:
            product = driver.find_element(By.ID, f"product{i}")
            product.click()
        except:
            pass


time = datetime.now()
time_limit = time + timedelta(minutes=30)

while game_on:
    current_time = datetime.now()
    second = datetime.now().second
    cookie.click()
    if second % 5 == 0 and datetime.now().microsecond > 500000:
        buy_upgrade()
        buy_item()
    if current_time > time_limit:
        game_on = False
    # items = driver.find_elements(By.CLASS_NAME, "products locked disabled")
    # print(items)
cookies = driver.find_element(By.ID, "cookies")
cookie_count = cookies.text.split()[0]
print(cookie_count)
driver.quit()