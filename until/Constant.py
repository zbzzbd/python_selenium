# -*- coding:utf-8 -*-
import ConfigParser

"""
常用的方法
"""
class Constant(object):

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

if __name__ =="__main__":
    sep,value=Constant().pase_element_find_method("xpath>//input")
    print sep,value