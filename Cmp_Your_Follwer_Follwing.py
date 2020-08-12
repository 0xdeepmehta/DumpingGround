
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

#Start the Firefox in headless Mode 
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# Let's do login 
print("\n[BOT] Let's do Login Riwaz\n")
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
element = driver.find_element_by_name('username')
# element.send_keys('username') # Type your UserName

element = driver.find_element_by_name('password')
# element.send_keys('password') # Type your Password

element.submit()
time.sleep(4)
print("[BOT] Login Riwaz Smpan Huwa\n\n")

print("[BOT] Let's Navigate to UserProfile \n")
userProfile = driver.get("https://www.instagram.com/imdeepmehta/")

print("[BOT] Let's Hunt Followers \n")
# follower link
url = "/imdeepmehta/followers/"

#find number of followers
allfoll=int(driver.find_element_by_xpath("//li[2]/a/span").text)
totalScrollFollwer = round(allfoll/12)

# open the follower windows
driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
time.sleep(1)

for i in range(totalScrollFollwer):
    if i <= 4:
        element_inside_popup = driver.find_element_by_xpath('//div[@class="_1XyCr"]//a')
        # Revel all the followers
        element_inside_popup.send_keys(Keys.END)
        time.sleep(1)
        print(".",end='')
        continue
    else:
        break

time.sleep(2)
# Extract the name of all the followers
elem = driver.find_element_by_xpath('//*[@class="PZuss"]')
all_li = elem.find_elements_by_tag_name("li")
totalFollower = []
for li in all_li:
    follower = li.find_element_by_css_selector(".MqpiF a")
    totalFollower.append(follower.text)
# close the popup follower Windos
driver.find_element_by_css_selector(".WaOAr .wpO6b").click()
print("[BOT] Done Hunting Followers \n ")


# Now Scrape Followeing
print("[BOT] Let's Hunt the Followeing \n")
url = "/imdeepmehta/following/"

#find number of followers
allfolling = int(driver.find_element_by_xpath("//li[3]/a/span").text)
totalScrollFollwing = round(allfolling/12)

# open the follower windows
driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
time.sleep(1)

for i in range(totalScrollFollwing):
    if i <= totalScrollFollwing:
        element_inside_popup = driver.find_element_by_xpath('//div[@class="isgrP"]//a')
        # Revel all the followers
        element_inside_popup.send_keys(Keys.END)
        print(".",end='')
        time.sleep(1)
        continue
    else:
        break

time.sleep(1)
# Extract the name of all the followers
elem = driver.find_element_by_xpath('//*[@class="PZuss"]')
all_li = elem.find_elements_by_tag_name("li")
totalFollowing = []
for li in all_li:
    following = li.find_element_by_css_selector(".MqpiF a")
    totalFollowing.append(following.text)
       
# close the popup follower Windos
driver.find_element_by_css_selector(".WaOAr .wpO6b").click()
print("[BOT] Done Hunting Following \n")


# Now Compare Your Follower vs Following
print("[BOT] These Idiots are not Follow you but You Do so Fuck YourSelf \n\n")
print(set(totalFollowing) - set(totalFollower))





