from bs4 import BeautifulSoup
from selenium import webdriver
import re # regex

#chrome driver, to open the browser
chromedriver = "/home/nissan/Desktop/PythonApps/parserTest/chromedriver"
driver = webdriver.Chrome(chromedriver)

#Change This
username = "find.freind.184"
emailLogin = 'yitzhak.sharon7@gmail.com'
passwordLogin = 'XXXXXXX'

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


# load page into beautiful soup
driver.implicitly_wait(5) # wait 5 seconds
print("waited 5 secs")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())


#redirect to friends
driver.get('https://www.facebook.com/'+username+'/friends')

#======== start extracting =======

friendsHTML = 'require("TimeSlice").guard((function(){bigPipe.onPageletArrive({bootloadable:{"ChatTypeaheadWrapper.react":{resources'

# bs = BeautifulSoup(friendsHTML, "html.parser")
# print (bs(text=re.compile('exact text')))
print("\n\n\n\n")
# for link in bs.find_all('id'):
#     print(link)
# txt = bs.script.get_text()
# friendID = re.match(r'{id:', txt).group(1)

# print(friendID)
# soup.find('script').text