import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import pandas as pd
options = uc.ChromeOptions()
options.user_data_dir = "chrome_profile"
driver = uc.Chrome(options=options)

driver.get('https://facebook.com')
input('enter to continue')

urls = pd.read_csv('import.csv').urls.tolist()
d=[]
try:
	for url in urls:
		driver.get('https://'+url)
		time.sleep(4)
		try:
			title = driver.title
		except:
			title = None
		try:
			website =driver.find_element_by_xpath('//div[contains(@style,"border-radius: max(")]//*[contains(@style,"-644px")]/following::div[1]//a').text
		except:
			website = None
		try:
			email = driver.find_element_by_xpath('//div[contains(@style,"border-radius: max(")]//*[contains(@style,"-539px")]/following::div[1]//a').text
		except:
			email = None
		try:
			phone = driver.find_element_by_xpath('//div[contains(@style,"border-radius: max(")]//*[contains(@style,"-502px")]/following::div[1]//span[text()]').text
		except:
			phone =None
		try:
			address =driver.find_element_by_xpath('//i[contains(@style,"background-position: 0px -582px")]/following::div[1]//span[text()]').text
		except:
			address =None
		try:
			extra = re.search(r'\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+[^jpg]\b',driver.page_source).group()
		except:
			extra =None
		data = {
		'url':url,
		'title':title,
		'website':website,
		'email':email,
		'phone':phone,
		'address':address,
		'extra':extra
		}
		d.append(data)
		print(f'{len(d)}/{len(urls)} | {data}')

finally:
	pd.DataFrame(d).to_csv('export.csv',index=False)