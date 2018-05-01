from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)

# options = Options()
# options.set_headless(headless=True)
username = "find.freind.184"
emailLogin = 'yitzhak.sharon7@gmail.com'
passwordLogin = 'Aa123456'

# driver.get('https://e-fibank.bg/EBank/Login')

# browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver')
driver = webdriver.Chrome(chromedriver)

#Open this site
driver.get('https://www.facebook.com/login.php')
print("Opened facebook...")

# Find element on login page and enter credentials
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(emailLogin)
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(passwordLogin)
print("Password entered...")

button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("FB opened")

friend = 'samuel.chemouny.9'
driver.get('https://www.facebook.com/'+friend+'/friends')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.implicitly_wait(5) # wait 5 seconds
print("waited 5 secs")




driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.implicitly_wait(5) # wait 5 seconds
print("waited 5 secs")
driver.implicitly_wait(5) # wait 5 seconds
print("waited 5 secs")

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())