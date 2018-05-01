from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui

import re # regex


def move_to_element(element, browser):
    action = webdriver.ActionChains(browser)
    action.move_to_element(element)
    action.perform()

def createGraph(username, level):
    if level == 0:
        return

    print("level" + str(level))

    # Enter to te friend of the "username" user
    driver.get('https://www.facebook.com/' + username + '/friends')

    # wait 3 seconds
    driver.implicitly_wait(5)

    # gets all friends of this user
    all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")

    i = 0
    while i < len(all_friends):
        # scroll to the element

        if i > 2:
            break

        move_to_element(all_friends[i], driver)

        # gets the link to the friend
        link = str(all_friends[i].get_attribute("href"))
        print(link)

        #check if the the connect between the users is exist
        #if not -->

        ####
        ####  Enter to the graph
        ####

        #  call recursion on the user-name
        vanity = all_friends[i].get_attribute("href")
        last = vanity.find('?')
        newUserName = vanity[25:last]
        print(newUserName)
        createGraph(newUserName, level - 1)

        # wait.until(lambda driver: "" != all_friends[i].text) # wait 3 seconds
        # all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")
        i = i + 1



#chrome driver, to open the browser
chromedriver = "/home/mcsa/PycharmProjects/untitled/chromedriver"
driver = webdriver.Chrome(chromedriver)

#Change This
username = "100025810568503"
emailLogin = 'roi.nacemani11111@gmail.com'
passwordLogin = 'Aa123456'

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

# load page
driver.implicitly_wait(5) # wait 5 seconds
print("waited 2 secs")

#redirect to friends\

createGraph(username,3)


