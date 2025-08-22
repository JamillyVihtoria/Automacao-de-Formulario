from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# abre o navegador e espera os elementos aparecerem
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
#Acessa o site
driver.get("https://demoqa.com/automation-practice-form")

#Localiza a div e preenche os campos
driver.find_element(By.ID, "firstName").send_keys("Jamilly")
time.sleep(2)
driver.find_element(By.ID, "lastName").send_keys("Barbosa")
time.sleep(2)
driver.find_element(By.ID, "userEmail").send_keys("email@exemplo.com")
time.sleep(2)

#Seleciona o Gênero
driver.find_element(By.XPATH, "//label[contains(text(),'Female')]").click()
time.sleep(2)

#Número de Telefone
driver.find_element(By.ID, "userNumber").send_keys("1234567890")
time.sleep(2)

#Data de Nascimento
date_input = driver.find_element(By.ID, "dateOfBirthInput")
date_input.click()
time.sleep(2)

# Selecionar mês, ano e dia (exemplo)
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").click()
driver.find_element(By.XPATH, "//option[text()='July']").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").click()
driver.find_element(By.XPATH, "//option[text()='2003']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='26']").click()
time.sleep(2)


#Hobbies
hobbies = ["Sports", "Reading", "Music"]
for hobby in hobbies:
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//*[contains(@class,'custom-checkbox') and .//*[contains(.,'{hobby}')]]//label")
    )).click()
time.sleep(2)

#Enviar o formulário
submit_btn = driver.find_element(By.ID, "submit")
time.sleep(2)
driver.execute_script("arguments[0].click();", submit_btn)
time.sleep(2)

driver.quit()
