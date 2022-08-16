from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import numpy as np
import pandas as pd

class Scraper:
    def __init__(self, url: str = 'https://www.imdb.com/'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    
    def accept_cookies()