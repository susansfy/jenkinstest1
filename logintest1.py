#-*-coding:utf-8 -*-
'''
Created on 

@author: susan


'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.action_chains import ActionChains


#login
driver = webdriver.Firefox()
driver.get("http://192.168.13.234/admin")
driver.maximize_window()
#wait
sleep(3)


username = (By.NAME,"userName")

passwd = (By.NAME,"password")


loginbtn = (By.XPATH,"//form[@id='frmLogin']/div[2]/footer/button")


search_in = (By.ID,"filterSearch")
search_btn = (By.ID,"addSearchBtn")

edit_btn = (By.XPATH,"//table[@id='datatable_fixed_column']/tbody/tr/td[10]/a")

pdf_tab = (By.XPATH,"//ul[@id='myTab']/li[2]/a/span")

add_pdf_btn = (By.XPATH,"//div[@id='DocumentTable']/div[1]/div/div[4]/a")

pdf_name = (By.XPATH,"//form[@id='frmDocumentSub']/div[1]/div/label/input")
pdf_upload_btn = (By.XPATH,"//form[@id='frmDocumentSub']/div[2]/div/div/div/div[3]/div/div[1]/a[1]")
pdf_path = "D:\\101.pdf"
pdf_save_btn = (By.XPATH,"//form[@id='frmDocumentSub']/div[6]/div/button")

home_page = (By.XPATH,"//aside[@id='left-panel']/nav/ul/li[1]/a/span")




driver.find_element(*username).send_keys("ava")
driver.find_element(*passwd).send_keys("123456")
driver.find_element(*loginbtn).click()
sleep(3)
print("login success")
