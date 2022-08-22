from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

""" Sets selenium chrome web driver.
    If you want a hadless driver set env to other thing than DEV into main.py """
def get_chrome( env = 'DEV' ):
  options = Options()
  options.add_argument("--disable-blink-features=AutomationControlled")

  if ( env == 'PROD' ):
    options.add_argument('--headless')

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

  return driver
