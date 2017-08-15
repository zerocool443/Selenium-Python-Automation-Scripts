from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("http://zzzscore.com/1to50/en")



driver.implicitly_wait(10)    

for number in range(1,51):
    for i in range(1,26):
        xpath='//*[@id="grid"]/div['+str(i)+']'
        elem = driver.find_element_by_xpath(xpath)
        inner_html=elem.get_attribute("innerHTML")
        
        try:
            number_in_the_box=inner_html.split("</span>")[1]
        except:
            number_in_the_box=0 
        if(int(number_in_the_box) == int(number)):
            print("gotch: "+str(number))
            xpath=xpath+"/span"
            elem = driver.find_element_by_xpath(xpath)
            elem.click()
            break
            