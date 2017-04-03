#Please use your username and password for academia in code
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome();
driver.get("https://academia.srmuniv.ac.in/")


driver.implicitly_wait(10)

iframe = driver.find_elements_by_css_selector('iframe')[0]
driver.switch_to.frame(iframe)

iframe2 = driver.find_elements_by_css_selector('iframe')[0]
driver.switch_to.frame(iframe2)

#Use of two iframe objects is because the form containing input field is inside an iframe which is inside an iframe 

username = driver.find_element_by_id("Email")
username.send_keys("username")
password = driver.find_element_by_id("Password")
password.send_keys("password")


driver.find_element_by_id("signinBtn").click();


driver.find_element_by_xpath('//*[@id="zc-container"]/tbody/tr[1]/td/div[5]/table/tbody/tr/td[8]').click();


time.sleep(10)


for i in range(4,12):
	for j in range(4,18):
		xpath_string='//*[@id="Student_Feedback_Form_2016_17_3"]/div[1]/form/div/table/tbody/tr/td/table/tbody/tr[6]/td/div/div[2]/table/tbody/tr['+str(i)+']/td['+str(j)+']/div/div[1]/li/span'
		temp=driver.find_element_by_xpath(xpath_string)
		temp.click()
		driver.execute_script("arguments[0].textContent = arguments[1]", temp, "Good")


for i in range(4,8):
	for j in range(4,17):
		xpath_string='//*[@id="Student_Feedback_Form_2016_17_3"]/div[1]/form/div/table/tbody/tr/td/table/tbody/tr[7]/td/div/div[2]/table/tbody/tr['+str(i)+']/td['+str(j)+']/div/div[1]/li/span'
		temp=driver.find_element_by_xpath(xpath_string)
		temp.click()
		driver.execute_script("arguments[0].textContent = arguments[1]", temp, "Excellent")


#driver.find_element_by_xpath('//*[@id="Student_Feedback_Form_2016_17_3"]/div[1]/form/table/tbody/tr/td/span/input[1]').click();		
