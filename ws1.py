import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path='/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
options1 = Options()
options1.add_argument('start-maximized')
options1.add_argument('disable-infobars')
driver.get('https://www.linkedin.com/home/')
mail = ''
password1 = ''
time.sleep(10)
driver.find_element(By.XPATH, "//input[@type= 'text']").send_keys(mail)
driver.find_element(By.XPATH, "//input[@type= 'password'][@name= 'session_password']").send_keys(password1)
driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button").click()
time.sleep(20)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3786873769&distance=25&geoId=106215326&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")
df = pd.DataFrame()
jt = []
jobs_blocks = driver.find_elements(By.XPATH, "//ul[contains(@class, 'scaffold-layout__list-container')]")


element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class, 'scaffold-layout__list-container')]"))
)

for job in element:
    driver.execute_script("arguments[0].scrollIntoView();", job)
    time.sleep(5)
job_links = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class, 'scaffold-layout__list-container')]//a[contains(@class, 'link job-card-list__title')]"))
)
for link in job_links:
    link.click()
    time.sleep(5)
    job_title = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/h2/a/span").text
    jt.append(job_title)

print("the name of the job is", jt)
