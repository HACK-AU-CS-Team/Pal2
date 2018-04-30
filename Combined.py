from bs4 import BeautifulSoup
from selenium import webdriver
import re # regex
from py2neo import Graph,Node,Relationship


graph = Graph(password="talmud18")
graph.delete_all()

#chrome driver, to open the browser
chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver)

#Change This

# username = "find.freind.184"
emailLogin = 'yitzhak.sharon7@gmail.com'
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


# load page into beautiful soup
driver.implicitly_wait(5) # wait 5 seconds
print("waited 5 secs")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())


#redirect to friends


#======== start extracting =======

print("start extracting")

def extract_friends(username, times_left): #times_left is for recursion
    if times_left==0: #stops recursion
        return



    driver.get('https://www.facebook.com/' + username + '/friends')
    driver.implicitly_wait(3)  # wait 3 seconds

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    print("currentpage:")
    print(driver.current_url)

    friendsHTML = r'require("TimeSlice").guard((function(){bigPipe.onPageletArrive({bootloadable:{"ChatTypeaheadWrapper.react":{resources'
    keywords_of_friends = r'ChatTypeaheadWrapper'
    #keywords_of_friends =  location = friends_tab
    tags = soup.find_all('script')
    for tag in tags:
        # print(tag)
        current_tag = str(tag)
        if keywords_of_friends in current_tag:
            # print(tag)
            # print("eurika")
            # startID = current_tag.find(r'{id:')
            # result = current_tag[startID + len('{id:')+len(r'"1008531709",name:"Samuel Chemouny",firstName:"Samuel",vanity:"samuel.chemouny.9"')]
            # print(str(result))

            my_string = current_tag
            ids = re.findall(r'{id:"[0-9]+',my_string)
            print(ids)

            vanitys = re.findall(r'vanity:"[a-zA-Z.0-9]+',my_string)
            print(vanitys)

            print("=========vanity===========")
            for match in vanitys:
                print(match[8:])
            print("=========id===========")
            for match in ids:
                print(match[5:])

            print("=========names===========")
            current_user = Node("Person", name=username, age=30)
            names = re.findall(r'name:"[a-zA-z ]+', my_string)
            for name in names:
                print(name[6:])
                person = Node("Person", name=name[6:], age=30)
                graph.create(person)
                graph.create(Relationship(current_user, "KNOWS", person))

            for match in vanitys:
                driver.implicitly_wait(5)  # wait 5 seconds
                print("waited 5 secs")
                extract_friends(match[8:], times_left - 1)


extract_friends("find.freind.184", 2)
