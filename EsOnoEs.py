import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


browser = webdriver.Firefox()
base_url = 'https://twitter.com/'
#query = '%23Brexit%20since%3A2017-06-01%20until%3A2017-06-03'
query =  'samantaacerenza'
Follow='/following'
fin= '?lang=en'
#url='https://twitter.com/search?q=%40samantaacerenza&src=typd&lang=en'
url = base_url + query+Follow

browser.get(url)
time.sleep(2)
time.sleep(30)

body = browser.find_element_by_tag_name('body')

followings = browser.find_elements_by_xpath('//div[@class="ProfileCard js-actionable-user"]')


seguidos = 0
i=0
while seguidos<len(followings):
    i+=1
    seguidos = len(followings)
    for _ in range(20):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
	followings = browser.find_elements_by_xpath('//div[@class="ProfileCard js-actionable-user"]')


    print i 

followings = browser.find_elements_by_xpath('//div[@class="ProfileCard js-actionable-user"]')



Siguiendo=[]
for follow in followings:
	try:	
		usuario = tweet.get_attribute('data-user-id')
		print usuario
		Siguiendo.append(usuario)	
	except:
		print('no salio')
	
print Siguiendo





