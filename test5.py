from bs4 import BeautifulSoup
from selenium import webdriver
import re # regex

#chrome driver, to open the browser
chromedriver = "../Pal2/chromedriver"
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
# print(soup.prettify())


#redirect to friends
driver.get('https://www.facebook.com/'+username+'/friends')

#======== start extracting =======
driver.implicitly_wait(3) # wait 3 seconds
print("start extracting")

friendsHTML = r'require("TimeSlice").guard((function(){bigPipe.onPageletArrive({bootloadable:{"ChatTypeaheadWrapper.react":{resources'
keywords_of_friends = r'ChatTypeaheadWrapper'
tags = soup.find_all('script')
for tag in tags:
    # print(tag)
    current_tag = str(tag)
    if keywords_of_friends in current_tag:
        print(tag)
        print("eurika")
        startID = current_tag.find(r'{id:')
        result = current_tag[startID + len('{id:')+len(r'"1008531709",name:"Samuel Chemouny",firstName:"Samuel",vanity:"samuel.chemouny.9"')]
        print(str(result))


# bs = BeautifulSoup(friendsHTML, "html.parser")
# print (bs(text=re.compile('exact text')))
print("\n\n\n\n")
# for link in bs.find_all('id'):
#     print(link)
# txt = bs.script.get_text()
# friendID = re.match(r'{id:', txt).group(1)

# print(friendID)
# soup.find('script').text