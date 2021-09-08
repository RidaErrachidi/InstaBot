from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

username = ''
password = ''

def __main__():
     driver = webdriver.Chrome(ChromeDriverManager().install())
     driver.get('https://www.instagram.com/accounts/login/')
     time.sleep(10)
     return

__main__()


     