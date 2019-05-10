# -*- coding: utf-8 -*-

import os
import codecs

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.firefox.options import Options as FirefoxOptions

from bs4 import BeautifulSoup



def selenium_chrome_options():
  options = webdriver.ChromeOptions()
  options.add_argument('--no-sandbox')
  options.add_argument('--headless')
  options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
  options.add_argument('--disable-gpu')
  options.add_argument('--window-size=1920, 1080')
  options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
  return options
def selenium_firefox_options():
  options = FirefoxOptions()
  options.headless = True
  return options

chrome_options = selenium_chrome_options()
chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedrivers/mac/chromedriver'))
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options) #replace with .Firefox(), or with the browser of your choice

# firefox_options = selenium_firefox_options()
# firefox_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'firefoxdrivers/mac/geckodriver'))
# browser = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# url = "https://www.dunelm.com/category/home-and-furniture/cook-and-dine/dining-and-tableware/glassware#facet?scroll=2030&pageSize=wide"
url = "http://www.forrentuniversity.com/The-University-of-Iowa"

browser.get(url) #navigate to the page

try:
  # Wait 20 seconds for page to load
  # timeout = 20
  # WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
  # # find_elements_by_xpath returns an array of selenium objects.
  # titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']") 
   
  # nav = browser.find_element_by_id("mainnav")
  # nav.text

  # # use list comprehension to get the actual repo titles and not the selenium objects.
  # titles = [x.text for x in titles_element]
  # # print out all the titles.
  # print('titles:')
  # print(titles, '\n')


  source_code = browser.execute_script("return document.body.parentElement.outerHTML") #returns the inner HTML as a string
  print('scrapped and saved..')
  print(source_code)
  file = codecs.open("scraped.html", "w", "utf-8")
  file.write(source_code)
  file.close()
  

  browser.close()
except TimeoutException:
  print("Timed out waiting for page to load")
  browser.quit()