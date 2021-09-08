from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = 'rida_e_'
password = 'Akram2003'

count = 0
driver
def login(driver):
     ## Replace with web driver wait
     driver.find_element_by_name("username").send_keys(username)
     driver.find_element_by_name("password").send_keys(password)
     driver.find_element_by_name("password").send_keys(u'\ue007')
def click_button_with_css(driver, css_selector):
     element = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
     )
def Find_Followers(driver):
     Scrolling_css = '[alt*="' + username + '"]'
     Profile_css = "[href*=\"" + username + "\"]"
     click_button_with_css(driver, Scrolling_css)
     click_button_with_css(driver, Profile_css)

def __main__():
     driver = webdriver.Chrome(ChromeDriverManager().install())
     driver.get('https://www.instagram.com/accounts/login/')
     time.sleep(1)
     login(driver)
     Find_Followers(driver)
     time.sleep(10000)

     Followers_css = "[href*=\"" + username + "/follwoers/\"]"
     css_select_close = '[aria-label="Close"]'
     following_css = "[href*=\"" + username + "/following/\"]"
     click_button_with_css((By.XPATH, "//button[contain(text(), 'Not Now')]"))

     click_button_with_css[driver, Followers_css]
     followers_list = Get_Usernames(driver)

     click_button_with_css(driver, css_select_close)
     time.sleep(1)

     click_button_with_css(driver, following_css)
     following_list = Get_Usernames(driver)


     return

def Check_Difference_In_Count(driver):
     global count
     new_count = len(driver.find_elements_by_xpath("//div[@role='dialog']//li"))

     if count != new_count:
          count = new_count
          return True
     else:
          return False


def Get_Usernames(driver):
     list_xpath = "//div[@role='dialog']//li"
     WebDriverWait(driver, 20).until(
          EC.presence_of_element_located((By.XPATH, list_xpath))

     )
     #scroll_down()

     list_elems = driver.find_elements_by_xpath(list_xpath)
     time.sleep(10000)
     users = []
     for i in range(len(list_elems)):
          try:
               row_text = list_elems[i].text
               if "Follow" in row_text:
                    username = row_text[:row_text.index("\n")]
                    users += [username]
          except:
               print("continue")
     return users

     
def Scroll_Down():
     global count
     iter = 0
     while 1:
          scroll_top_num = str(iter * 1000)
          iter += 1
          driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollTop= "+ scroll_top_num)

          try:
               WebDriverWait(driver, 1).until(Check_Difference_In_Count)
          except:
               count = 0
               break


__main__()


     