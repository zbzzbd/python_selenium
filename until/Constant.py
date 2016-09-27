# -*- coding:utf-8 -*-
import ConfigParser

"""
页面上常用的方法
"""
class Constant(object):

    def open_url(self,driver,url):
        driver.get(url)
 

    def Read_file_init(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('D:\\code\\dx_py_auto_selenium\\element.ini'))
        print config.items('login')
        username=config.get('login','username')
        passw =config.get('login','passw')
        logtn =config.get('login','submit')
        return username,passw,logtn

    def pase_element_find_method(self,str):
        list=str.split('>')
        spetator=list[0]
        value =list[1]
        return spetator,value

    def according_type_find_element(self,driver,str,value):
        if str=='xpath':
            return driver.find_element_by_xpath(value)
        if str =='css':
            return driver.find_element_by_class_name(value)


if __name__ =="__main__":
    sep,value=Constant().pase_element_find_method("xpath>//input")
    print sep,value