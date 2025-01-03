from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import random

accouts_excel = 'v_hub_accounts.xls'
cols_accounts = [
    'email_id',
    'account_group',
    'account_grade',
    'account_name',
    'gender',
    'account_tel'
]

dtype_accounts = {
    'email_id':str, 
    'account_group':str, 
    'account_grade':str, 
    'account_name':str, 
    'gender':str, 
    'account_tel':str
}

def accouts_excel_to_list(accouts_excel):
    df = pd.read_excel(accouts_excel, engine='openpyxl', usecols='D:I', sheet_name=0, names=cols_accounts, dtype=dtype_accounts)
    df = df.fillna('empty_data')
    account_emails = df['email_id'].tolist()
    account_names = df['account_name'].tolist()
    account_tels = df['account_tel'].tolist()
    return df, account_emails, account_names, account_tels

accounts_excel_data = accouts_excel_to_list(accouts_excel)
account_emails = accounts_excel_data[1]
account_names = accounts_excel_data[2]
account_tels = accounts_excel_data[3]

accounts_input = []
test_input = [
    'miku_love_3939_hatsune_1@gmail.com',
    'mikumiku3939!@',
    'mikumiku3939!@',
    'Hatsune39',
    '하춘혜',
    '01039390831'
]

test_input1 = [
    'miku_love_3939_hatsune_2@gmail.com',
    'mikumiku3939!@1',
    'mikumiku3939!@1',
    'megurine',
    '하춘혜',
    '01039390831'
]
accounts_input.append(test_input)
accounts_input.append(test_input1)


for i in range(len(accounts_excel_data[0])):
    account_tel = account_tels[i]
    if account_tel != 'empty_data':
        account_input = []

        pwd_input = account_tels[i]+'asd!@#'
        pwd_confirm = pwd_input

        account_nick = account_names[i]
        account_name = account_names[i]

        account_input.append(account_emails[i])
        account_input.append(pwd_input)
        account_input.append(pwd_confirm)
        account_input.append(account_nick)
        account_input.append(account_name)
        account_input.append(account_tel)

        accounts_input.append(account_input)

for i in accounts_input:
    print(i)
print(len(accounts_input))
print('\n')
for i in accounts_input[:3]:
    print(i)

signin_input_xpaths = [
    '//*[@id="input-email"]',
    '//*[@id="input-password"]',
    '//*[@id="input-password-checked"]',
    '//*[@id="input-nick"]',
    '//*[@id="input-name"]',
    '//*[@id="input-tel"]'
]

driver = webdriver.Chrome('chromedriver.exe')

url = 'https://v-hub.store/'
driver.get(url)

for account in accounts_input[:3]:
    x_login = '//*[@id="fixed-menu"]/li[2]/a[1]/span[2]'
    text_panel = driver.find_element(By.XPATH, x_login)
    text_panel.click()
    sleep(1)

    x_signup = '//*[@id="no-fouc"]/body/div[2]/div[2]/div/div/div[3]/div[1]/a[2]'
    input_window = driver.find_element(By.XPATH, x_signup)
    input_window.click()
    sleep(1)

    for i in range(len(signin_input_xpaths)):
        x_input = signin_input_xpaths[i]
        txt_panel = driver.find_element(By.XPATH, x_input)
        txt_panel.click()
        txt_panel.send_keys(account[i])

    x_agree_signup = '//*[@id="no-fouc"]/body/div[2]/div[2]/div/div/div[2]/div/div/a'
    signup_panel = driver.find_element(By.XPATH, x_agree_signup)
    signup_panel.click()
    sleep(1)

    alert_msg = driver.switch_to.alert.text
    driver.switch_to.alert.accept()
    sleep(1)

    x_dropdown = '//*[@id="fixed-menu"]/li[2]/a[2]/span[2]'
    dropdown_element = driver.find_element(By.XPATH, x_dropdown)
    hover_dropdown = ActionChains(driver)
    hover_dropdown.move_to_element(dropdown_element).perform()
    sleep(0.1)

    x_logout = '//*[@id="fixed-menu"]/li[2]/ul/li[5]/a'
    logout_panel = driver.find_element(By.XPATH, x_logout)
    logout_panel.click()
    sleep(1)

driver.close()