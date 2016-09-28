# -*-coding:utf-8 -*-
"""
本函数主要撰写常用工具，比如：截图
"""
import  os
from selenium import  webdriver

def insert_img(driver,filename):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    print base_dir
    base_dir = base_dir.replace('\\','/')
    print base_dir

    #base = base_dir.split('/testCase')[0]

    file_path = base_dir + "\\report\\image\\" +filename

    driver.get_screenshot_as_file(file_path)

if __name__ == "__main__":
    driver=webdriver.Firefox()
    driver.get("http://www.ggang.cn")
    insert_img(driver,'ggang.jpg')
    driver.quit()