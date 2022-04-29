from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


driver = webdriver.Chrome('/Users/mac/Desktop/pythonProject/chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://aviata.kz/')

from_to_button = driver.find_element(By.CLASS_NAME, 'ux-searchform-roundtrip').click()
wait = WebDriverWait(driver, 10)
searchBoxFrom = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="ux-pop-orig js-is-orig"][data-code="ALA"]'))).click()


searchBoxTo = wait.until(ec.element_to_be_clickable((By.XPATH, '//span/a[@class="ux-pop-dest"][3]'))).click()

datePicker1 = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'input[placeholder="Дата отправления"]'))).click()
to_date = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[4]/td[2]/a'))).click()

datePicker2 = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Когда обратно"]'))).click()
back_date = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[5]/td[4]/a'))).click()

searchPassengers = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="form-control inputfield__grey"]'))).click()

selectPassengers = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="searchpassengers__select"]')))
buttonYouth = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-class="youths"]'))).click()
buttonPlus = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'button[class="btn-circle btnPlus ux-searchform-youth-plus success"]'))).click()
clickclick = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="container3 flightsearch"]'))).click()

buttonFind = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="btnCustom btnCustom-default btnGreen flightsearch__findbutton ux-main-search"]'))).click()


time.sleep(10)
driver.quit()


