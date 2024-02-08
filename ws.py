import time
import pandas as pd
import os
from selenium import webdriver

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=option)
url = (
    'https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3778850066https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3778850066')
# driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
# service = Service(executable_path='./chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
# print("options", options)
# driver=webdriver.Chrome()
# print("driver", driver)
# driver.implicitly_wait(10)
# driver.get(url)
# driver = webdriver.Chrome()
#
# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

service = Service(executable_path='/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
options1 = Options()
options1.add_argument('start-maximized')
options1.add_argument('disable-infobars')
driver.get('https://www.linkedin.com/jobs/')

# driver.get('https://www.linkedin.com/jobs/search/?alertAction=viewjobs&currentJobId=3780614159&distance=25&f_TPR'
#            '=a1702378819-&geoId=106215326&keywords=python%20developer&origin=JOB_ALERT_IN_APP_NOTIFICATION&savedSearchId'
#            '=1728180890&sortBy=R')
# driver.quit()

time.sleep(10)
# driver.implicitly_wait(100)
# driver.get(url)
y = driver.find_element(By.ID, 'results-list__title')[0].text

print('value of y is :', y)
