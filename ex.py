"""import requests
from bs4 import BeautifulSoup
page = requests.get('http://pythonscraping.com/pages/page3.html')
html = page.text # Get the content of the webpage
#soup = BeautifulSoup(html, 'html.parser') # Convert that into a BeautifulSoup object that contains methods to make the tag searcg easier
print(html)"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
driver.get(URL)
time.sleep(2) # Wait a couple of seconds, so the website doesn't suspect you are a bot
try:
    driver.switch_to_frame('gdpr-consent-notice') # This is the id of the frame
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
    accept_cookies_button.click()

except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
    driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
    accept_cookies_button.click()

except:
    pass
time.sleep(2)
house_property = driver.find_element(by=By.XPATH, value='//*[@id="listing_62117651"]') # Change this xpath with the xpath the current page has in their properties
a_tag = house_property.find_element_by_tag_name('a')
link = a_tag.get_attribute('href')
print(link)
driver.get(link)
