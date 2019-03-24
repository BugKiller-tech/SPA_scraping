# -*- coding: utf-8 -*-

import os
import codecs

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException



def selenium_options():
  options = webbrowser.ChromeOptions()
  options.add_argument("--incognito")
  return options

options = selenium_options()
chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedrivers/mac/chromedriver'))


browser = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=option) #replace with .Firefox(), or with the browser of your choice
# browser = webdriver.Firefox()
url = "https://www.dietprobe.com/cabbage-soup-diet/"
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
  file = codecs.open("scraped.html", "w", "utf-8")
  file.write(source_code)
  file.close()
  

  browser.close()
except TimeoutException:
  print("Timed out waiting for page to load")
  browser.quit()