from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)

options = Options()
options.set_headless(headless=True)

driver.get('https://e-fibank.bg/EBank/Login')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver')

print("Opened Page...")

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())

