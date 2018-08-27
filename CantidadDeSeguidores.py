# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 00:19:27 2017

@author: Fede
"""
# https://medium.com/@dawran6/twitter-scraper-tutorial-with-python-requests-beautifulsoup-and-selenium-part-2-b38d849b07fe
"""
* dia brexit: 06/23/2016 hasta: 04/23/2016 

* hashtags a scrapear: #brexit, #EUref, #VoteLeave, #LeaveEU, #Strongerin  
http://hashtagify.me/hashtag/brexit
http://ukandeu.ac.uk/how-remain-and-leave-camps-use-hashtags/


* querys a usar (cerca de londres):
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-20%20until%3A2016-06-23'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-17%20until%3A2016-06-20'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-14%20until%3A2016-06-17'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-11%20until%3A2016-06-14'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-08%20until%3A2016-06-11'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-05%20until%3A2016-06-08'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-06-02%20until%3A2016-06-05'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-05-31%20until%3A2016-06-02'
'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-05-28%20until%3A2016-05-31' tiene 98


'%23brexit%20OR%20%23EUref%20OR%20%23VoteLeave%20OR%20%23LeaveEU%20OR%20%23Strongerin%20near%3A%22London%2C%20England%22%20within%3A15mi%20since%3A2016-04-23%20until%3A2016-06-23'


"""

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

archivo_excel = pd.read_excel('usuarios.xlsx')
usuarios = archivo_excel.values



for usuario in usuarios:
	if str(usuario[1])=='nan':
		
		f= open('CantidadSeguidores.txt', 'a')
		f.write("{ 'usuario': "+str(usuario) +", 'Cantidad_De_Tweets': 0, 'Following': 0, 'Followers':0, 'Likes':0} \n")
		f.close() 
	else:
		try:	
			browser = webdriver.Firefox()

			base_url = 'https://twitter.com/'
			#query = '%23Brexit%20since%3A2017-06-01%20until%3A2017-06-03'
			query = str(usuario[1]) 
			fin= '?lang=en'
			#url='https://twitter.com/search?q=%40samantaacerenza&src=typd&lang=en'
			url = base_url + query +fin

			browser.get(url)
			time.sleep(2)
			browser.get(url)
			time.sleep(2)


			InfoSeguidores = browser.find_elements_by_xpath('//span[@class="ProfileNav-value"]')

			datos=[0]*8
			i=0
			for info in InfoSeguidores:
				datos[i]= info.get_attribute('data-count')
				i+=1


			f= open('CantidadSeguidores.txt', 'a')

			f.write("{ 'usuario': "+str(usuario) +", 'Cantidad_De_Tweets': "+str(datos[0])+", 'Following': "+str(datos[1])+", 'Followers': "+str(datos[2])+", 'Likes': "+str(datos[3])+'} \n')


			f.close() 

			
		except:
			print str(usuario[0])+ 'fallo'
		
		browser.quit()

