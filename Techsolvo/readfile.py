import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
def reading():

    df = pd.read_csv('/home/superadmin/DBDA/Techsolvo/sample-data-india.csv',usecols=['Company','Phone'])
    return df

def driver(df):
    browser = webdriver.Chrome()
    browser.get('https://www.go4worldbusiness.com/')
    ## find the search box on the website
    path = '/html/body/div[4]/di/div[1]/div/form/div[2]/div/input'
    butn = '/html/body/div[4]/di/div[1]/div/form/div[3]/button[2]'
    try:
        for cmpny in df['Company'].unique():
            browser.find_element_by_xpath(path).clear()
            browser.find_element_by_xpath(path).click()
            browser.find_element_by_xpath(path).send_keys(cmpny)
            browser.find_element_by_xpath(butn).send_keys(Keys.ENTER)
            ## path to look for company name
            cmpny1=browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[1]/div/h1/span').text
            browser.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[2]/div/div')
            ## find all first company name come on searching
            browser.find_elements_by_tag_name('a')
            test = browser.find_element_by_tag_name('h2').text
            if cmpny in test:
                print("Company matched")
                time.sleep(5)

            else:
                print("Not matched")
            print(cmpny, " == ", test)
            path = '/html/body/div[1]/div/form/div[2]/div/input'
            butn = '/html/body/div[1]/div/form/div[3]/button[2]'
    except :
        print("Path not found")
    finally:
        time.sleep(3)
        browser.implicitly_wait(0)

df = reading()
driver(df)
