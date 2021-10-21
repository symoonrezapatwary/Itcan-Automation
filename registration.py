from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.itcanapp.com/signup')
time.sleep(3)
def reg(e):
    count=0
    time.sleep(2)
    input_mail = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[1]/div/input')
    input_mail.send_keys(e)

    countinue_button = driver.find_element_by_xpath('//*[@id="basic"]/div[2]/div/div/div/div/button/span')
    countinue_button.click()
    time.sleep(5)
    # if count==0:
    #     print("Registration Successfull")
    #     count=4
    #     time.sleep(3)
    #     breakpoint
    email_alreadyexists = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[2]/div')
    email_alreadyexistsAlert = email_alreadyexists.text
    invalid_mail_msg = driver.find_element_by_xpath('//*[@id="basic"]/div[1]/div/div/div[2]/div')  
    invalid_mail_msgText = invalid_mail_msg.text
    time.sleep(3)
    if email_alreadyexistsAlert:
        print(email_alreadyexistsAlert)
        time.sleep(3)
        driver.get('https://www.itcanapp.com/signup')
        print('Test Successful')
        drive('forhadrezapatwar@gmail.com')
        breakpoint
       
        time.sleep(5)
        count =2
        google_login()
        
    
    elif invalid_mail_msgText:
        print(invalid_mail_msgText)
        time.sleep(3)
        breakpoint
    else:
        print('Test Successfull')

        
   
    

def drive(e):
    reg(e)
drive('sohanrezapatawagmail.com')
# def reloadregpage():
#     driver.get('https://www.itcanapp.com/signup')
def google_login():
    cookie = driver.get_cookies()
    delete_cookie = driver.delete_all_cookies()
    driver.get('https://www.itcanapp.com/signup')
    time.sleep(5)
    continue_with_google = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div/div[2]/div[1]/div[1]/div[3]/div/div/div/div[2]')
    continue_with_google.click()
    print("Proceed With Google Login")
google_login()

   