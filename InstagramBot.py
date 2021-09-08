from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = 'rida_e_'
password = 'Akram2003'

def login(driver):
     ## Replace with web driver wait
     driver.find_element_by_name("username").send_keys(username)
     driver.find_element_by_name("password").send_keys(password)
     driver.find_element_by_name("password").send_keys(u'\ue007')
def click_button_with_css(driver, css_selector):
     element = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
     )
def FindFollowers(driver):
     Scrolling_css = '[alt*="' + username + '"]'
     Profile_css = "[href*=\"" + username + "\"]"
     click_button_with_css(driver, Scrolling_css)
     click_button_with_css(driver, Profile_css)

def __main__():
     driver = webdriver.Chrome(ChromeDriverManager().install())
     driver.get('https://www.instagram.com/accounts/login/')
     time.sleep(1)
     login(driver)
     FindFollowers(driver)
     time.sleep(10000)

     return

__main__()


     