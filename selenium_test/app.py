import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException



chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver'))
print(chrome_driver_path)
browser = webdriver.Chrome(chrome_driver_path) #replace with .Firefox(), or with the browser of your choice
# browser = webdriver.Firefox()
url = "http://example.com/login.php"
browser.get(url) #navigate to the page
browser.close()