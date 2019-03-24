# -*- coding: utf-8 -*-

import os
import datetime
import codecs

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

def write_to_file(source_code):
  file = codecs.open("scraped.html", "w", "utf-8")
  file.write(source_code)
  file.close()


def selenium_options():
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  return options

chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedrivers/mac/chromedriver'))
def scrap_url(url):
  try:
    options = selenium_options()
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options) #replace with .Firefox(), or with the driver of your choice
    print('implicity wait', datetime.datetime.now())
    driver.implicitly_wait(30)
    print('end of implicity wait', datetime.datetime.now())
    driver.get(url) #navigate to the page
    # time.sleep(2.5) #Wait for javscript to load in Selenium this doesn't needed now
    # source_code = driver.execute_script("return document.body.parentElement.outerHTML") #returns the inner HTML as a string
    # source_code = driver.page_source.encode('utf-8')

    source_code = driver.page_source
    driver.close()
    write_to_file(source_code)
    driver.quit()
    print('completed scraping with headless browser')
  except TimeoutException:
    print("Timed out waiting for page to load")


url = "https://intersport.com.au/"
scrap_url(url)


