from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# add credentials
E_MAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# set driver
driver = webdriver.Chrome(chrome_options)
driver.get("https://www.linkedin.com/jobs/search/"
           "?currentJobId=3852945046&f_AL=true&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

sign_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_btn.click()

# login in linkedIn
email_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
sign_up_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")

email_input.send_keys(E_MAIL)
password_input.send_keys(PASSWORD)
sign_up_btn.click()

# find jobs
time.sleep(1)
jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
print(len(jobs))

for job in jobs:
    time.sleep(1)
    job.click()
    time.sleep(1)
    apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
    apply_btn.click()

    time.sleep(1)
    dismiss_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
    dismiss_btn.click()

    time.sleep(1)
    discard_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button")
    discard_btn.click()

time.sleep(1)
driver.quit()
