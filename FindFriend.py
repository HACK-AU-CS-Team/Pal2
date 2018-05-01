from bs4 import BeautifulSoup
from selenium import webdriver
import re # regex


def move_to_element(element, browser):
    action = webdriver.ActionChains(browser)
    action.move_to_element(element)
    action.perform()


#chrome driver, to open the browser
chromedriver = "/home/mcsa/PycharmProjects/untitled/chromedriver"
driver = webdriver.Chrome(chromedriver)

#Change This
username = "100025713531512"
emailLogin = 'roiaa654321@gmail.com'
passwordLogin = 'rughbjnbh'

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

#####
# all_friends = driver.find_elements_by_css_selector("a[dir='ltr']")
# for friend in all_friends:
#     link= friend.find_element("href")
#     name = friend.text
# email.send_keys(emailLogin)
# print("Email Id entered...")
# password = driver.find_element_by_xpath("//input[@id='pass']")
# password.send_keys(passwordLogin)
# print("Password entered...")

####

button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("FB opened")


# load page
driver.implicitly_wait(5) # wait 5 seconds
print("waited 2 secs")


#redirect to friends
driver.get('https://www.facebook.com/'+username+'/friends')

#======== start extracting =======
driver.implicitly_wait(5) # wait 3 seconds
print("start extracting")
#data-hovercard-prefer-more-content-show

all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")
# all_friends = driver.find_elements_by_css_selector("a")
# print(len(all_friends))
i=0
while i< len(all_friends):
    # link= friend.find_element("href")
    # name = friend.text
    # link = friend.find_element("data-hovercard-prefer-more-content-show")
    #if i%2 ==1:
    move_to_element(all_friends[i],driver)
    driver.implicitly_wait(5)  # wait 3 seconds
    print(all_friends[i].text)
    all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")

    i=i+1

