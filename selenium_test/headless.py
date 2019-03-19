# -*- coding: utf-8 -*-

import os
import codecs

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

def write_to_file(text):
  file = codecs.open("scraped.html", "w", "utf-8")
  file.write(source_code)
  file.close()


options = webdriver.ChromeOptions()
options.add_argument('headless')
chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedrivers/mac/chromedriver'))
browser = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options) #replace with .Firefox(), or with the browser of your choice

try:
  url = "https://bvopen.abrickis.me/#/standings"
  browser.get(url) #navigate to the page

  source_code = browser.execute_script("return document.body.parentElement.outerHTML") #returns the inner HTML as a string
  browser.close()
  
  write_to_file(source_code)
  print('completed scraping with headless browser')

except TimeoutException:
  print("Timed out waiting for page to load")
  browser.quit()