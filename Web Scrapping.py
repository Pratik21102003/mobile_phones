from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Define the driver path
driver_path = Service("c:/Users/Pratik/Desktop/chromedriver.exe")

# Set the different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) 
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Ignore the certificate and SSL errors
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Maximize the browser window
#chrome_options.add_argument("start-maximized")

# Define the driver and open the browser
driver = webdriver.Chrome(service=driver_path, options=chrome_options) 
driver.get('https://www.smartprix.com/mobiles')
old_hieght=driver.execute_script('return document.body.scrollHeight')
while True:
   time.sleep(4)
   driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
   time.sleep(2)
   new_hieght=driver.execute_script('return document.body.scrollHeight')
   if old_hieght==new_hieght:
       break
   else:
       old_hieght=new_hieght
html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)