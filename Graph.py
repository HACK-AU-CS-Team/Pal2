from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from py2neo import Graph,Node,Relationship
from random import randint
import time

def move_to_element(element, browser):
    action = webdriver.ActionChains(browser)
    action.move_to_element(element)
    action.perform()

def createGraph(username, level):
    if level == 0:
        return

    print("level" + str(level))
    driver.implicitly_wait(3)

    # Enter to te friend of the "username" user
    driver.get('https://www.facebook.com/' + username + '/friends')

    # wait 3 seconds
    driver.implicitly_wait(5)

    # gets all friends of this user
    all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")

    i = -1
    while i < len(all_friends):
        # scroll to the element

        driver.implicitly_wait(3)

        i = i + 1
        if i % 2 == 0:
            continue

        # driver.implicitly_wait(3)

        # move_to_element(all_friends[i], driver)

        # gets the link to the friend
        driver.get('https://www.facebook.com/' + username + '/friends')

        all_friends = driver.find_elements_by_css_selector("a[href$='fref=pb&hc_location=friends_tab']")
        print(len(all_friends))
        print(i)
        link = str(all_friends[i].get_attribute("href"))
        print(link)

        #check if the the connect between the users is exist
        #if not -->

        ####
        ####  Enter to the graph
        ####

        #  call recursion on the user-name
        vanity = all_friends[i].get_attribute("href")
        newUserName = ""

        if "profile.php?id=" not in vanity:
            last = vanity.find('?')
            newUserName = vanity[25:last]
            print("vanity:")
            print(newUserName)
        else:
            last = vanity.find('&')
            newUserName = vanity[40:last]
            print("vanity:")
            print(newUserName)

        print(newUserName)

        current_user = Node("Person", name=username, age=30)
        person = Node("Person", name=newUserName, age=30)
        temp = graph.run("Match (n:Person {name:'%s'}) return n;" % (newUserName))
        if temp.data().__len__() == 0:
            print("111111")
            graph.create(person)
            graph.create(Relationship(current_user, "KNOWS", person))
            graph.create(Relationship(person, "KNOWS", current_user))
        #   graph.run("CREATE (m:Person  {name:'%s'})WITH m MATCH (u:Person { username: '%s' }) CREATE(m)-[r:POSTED_BY]->(u) RETURN m);" %newUserName;
        else:
            print("2222222")
            # graph.run("MERGE (u:Person { name:'%s'}) MERGE (m:Person { name:'%s'}) MERGE (m)-[r:POSTED_BY]->(u) RETURN m,r,u);" % (newUserName) ,(username))
            # graph.run("MERGE (u:Person { name:'%s'}) MERGE (m:Person { name:'%s'}) MERGE (m)-[r:POSTED_BY]->(u) RETURN m,r,u);" % (username) , (newUserName))
            mystr = "MERGE (u:Person { name:'%s'}) MERGE (m:Person { name:'%s'}) MERGE (m)-[r:POSTED_BY]->(u) RETURN m,r,u;" % (
                newUserName, username)
            #  graph.run("MERGE (u:Person { name:'%s'}) MERGE (m:Person { name:'%s'}) MERGE (m)-[r:POSTED_BY]->(u) RETURN m,r,u);" % ((username) , (newUserName)))


        time.sleep(randint(2,9))

        createGraph(newUserName, level - 1)


graph =Graph(password="Aa123456")
#chrome driver, to open the browser
chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)


#Change This
username = "amit.dvirhacker.7"
emailLogin = 'amitdvirishacker@outlook.co.il'
passwordLogin = 'Rr123456'

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
myst2 = "MATCH (n:Person) WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count WHERE count > 1 CALL apoc.refactor.mergeNodes(nodelist) YIELD node RETURN node;"

graph.run((myst2))

createGraph(username,4)
#graph.run("MATCH p=shortestPath((s1:Person {name:'yitzhak.sharon.1'})-[*]-(s2:Person {name:'1475314557'})) RETURN p")


