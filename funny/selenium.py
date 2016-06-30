from BeautifulSoup import BeautifulSoup
from selenium import webdriver

website = 'http://xueshu.baidu.com/s?wd=paperuri%3A%28149b8284018cb151a8debf8664955493%29&filter=sc_long_sign&sc_ks_para=q%3DCross-organization%20Task%20Coordination%20Patterns%20of%20Urban%20Emergency%20Response%20Systems&sc_us=17403480238996714361&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8'
driver = webdriver.Firefox()
driver.get(website)
driver.maximize_window()

while True:
	try:
		driver.find_element_by_class_name("c-icon-triangle-down-d").click()
		break
	except:
		driver.refresh()

html_source = driver.page_source
soup = BeautifulSoup(html_source)
for sub in soup.findAll('p',attrs={'class':'abstract'}):
	print sub.string
