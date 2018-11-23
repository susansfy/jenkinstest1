#-*-coding:utf-8 -*-
'''
Created on 2018年8月8日

@author: susan

为学生添加文档
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.action_chains import ActionChains


#登录
driver = webdriver.Firefox()
driver.get("http://192.168.13.243/admin")
driver.maximize_window()
#点击登录按钮进入登录界面
sleep(3)

#元素集
#用户名
username = (By.NAME,"userName")
#密码
passwd = (By.NAME,"password")

#登录 按钮
loginbtn = (By.XPATH,"//form[@id='frmLogin']/div[2]/footer/button")

#搜索输入框
search_in = (By.ID,"filterSearch")
search_btn = (By.ID,"addSearchBtn")
#编辑按钮
edit_btn = (By.XPATH,"//table[@id='datatable_fixed_column']/tbody/tr/td[10]/a")
#文档tab
pdf_tab = (By.XPATH,"//ul[@id='myTab']/li[2]/a/span")
#添加按钮
add_pdf_btn = (By.XPATH,"//div[@id='DocumentTable']/div[1]/div/div[4]/a")
#添加界面
pdf_name = (By.XPATH,"//form[@id='frmDocumentSub']/div[1]/div/label/input")
pdf_upload_btn = (By.XPATH,"//form[@id='frmDocumentSub']/div[2]/div/div/div/div[3]/div/div[1]/a[1]")
pdf_path = "D:\\101.pdf"
pdf_save_btn = (By.XPATH,"//form[@id='frmDocumentSub']/div[6]/div/button")
#首页
home_page = (By.XPATH,"//aside[@id='left-panel']/nav/ul/li[1]/a/span")




driver.find_element(*username).send_keys("ava")
driver.find_element(*passwd).send_keys("123456")
driver.find_element(*loginbtn).click()
sleep(3)
print("login success")