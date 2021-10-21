from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.itcanapp.com/login')
time.sleep(3)

def login(e,p):
    count = 0

    email = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[1]/div/input')
    #email.send_keys("")
    email.send_keys(e)
    password =driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div[1]/div/span/input')
    password.send_keys(p)
    start_button = driver.find_element_by_xpath('//*[@id="basic"]/div[3]/div/div/div/div/button/span')
    start_button.click()
    time.sleep(5)
    if count==0:
        print('Test 1 Successfull')
        time.sleep(2)
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[1]/div/div[1]/div[2]/div/div[6]/div'))).click()

    #     self.driver.find_element_by_xpath("//select[@name='loan_purpose']/option[text()='Home Renovation']").click() 
    # email_field_req_msg = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[2]/div')
    cookie = driver.get_cookies()
    delete_cookie = driver.delete_all_cookies()
    driver.get('https://www.itcanapp.com/login')
    time.sleep(5)
    # continue_with_google = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[2]')
    # continue_with_google.click()
    
    # time.sleep(2)
    # driver.get('https://accounts.google.com/o/oauth2/auth/identifier?redirect_uri=storagerelay%3A%2F%2Fhttps%2Fwww.itcanapp.com%3Fid%3Dauth204107&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=230434675739-bgc01e00il5ln8ligllbqlr2ui39nfph.apps.googleusercontent.com&ss_domain=https%3A%2F%2Fwww.itcanapp.com&prompt&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow')
    # input_gmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
    # input_gmail.send_keys('symoonrezapatwaryanik@gmail.com')
    # time.sleep(2)
    # next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
    # next_button.click()
    # time.sleep(2)
    drive('bivor@6sensehq.com','123456')
    breakpoint


    email_field_req_msgText =  email_field_req_msg.text
    if email_field_req_msgText:
        print(email_field_req_msgText)
        print('Test 2 successfull')
        count=1
        breakpoint
       
    password_field_msg = driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div[2]/div')
    password_field_msgText = password_field_msg.text
    if password_field_msgText:
        print(password_field_msgText)
        print('Test 3 Successful')
        count=2
    password_char = driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div[2]/div')
    password_char_msg = password_char.text
    if password_char_msg:
        print(password_char_msg)
        print('Test 4 Successfull')

    
    userNOtFound = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[2]/div')
    userNOtFoundText = userNOtFound.text
    if userNOtFoundText:
        print(userNOtFoundText)
        forget_password = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div/div[2]/div[1]/div[3]/div/a')
        forget_password.click()
        print('Test 5 Successfull')
        time.sleep(2)
        forget_email_input = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[1]/div/input')
        forget_email_input.send_keys('symoon@6sensehq.com')
        send_reset_link_button = driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div/div/button/span')
        send_reset_link_button.click()
        print('Test 0 successfull')
        count =3
        


  
        
        

        
        
    # count = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[2]')
    # countText = count.text
def drive(email, password):
    login(email, password)

drive('furycristianosymoon@gmail.com','Symoon232skylarks')

