import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import locator

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
url = "https://play.google.com/store/apps/details?id=com.bitoex.bitoproapp"
driver = webdriver.Chrome((ChromeDriverManager().install()), options=option)
driver.get(url)


def get_android_version():
    about_this_app = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator.ABOUT_THIS_APP)))
    # Scroll down window
    driver.execute_script("arguments[0].focus();", about_this_app)
    about_this_app.click()
    time.sleep(1)
    android_version = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, locator.ANDROID_VERSION)))
    print("android_version: " + android_version.text)
    return android_version.text


def get_ios_version():
    new_url = "https://apps.apple.com/tw/app/bitopro/id1393007496"
    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[1])
    driver.get(new_url)
    ios_version = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, locator.IOS_CURRENT_VERSION)))
    print("iOS_version: " + ios_version.text)
    current_version = ios_version.text.split()
    return current_version[1]


def compare_version():
    assert get_android_version() == get_ios_version(), "Different versions!!"
    driver.quit()


if __name__ == '__main__':
    compare_version()
