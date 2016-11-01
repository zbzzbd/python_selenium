# -*- coding:utf-8 -*-
import ConfigParser
import os
import  string

"""
常用的方法
"""
class Constant(object):
    def __init__(self):
        self.filename=self.Read_file_config('file').get('filename')

    def Read_file_init(self,item):
        file_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config = ConfigParser.ConfigParser()
        config.readfp(open(file_dir+'/'+self.filename))
        #print config.items(item)
        return dict(config.items(item))

    def Read_file_config(self,item):
        file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config = ConfigParser.ConfigParser()
        config.readfp(open(file_dir + '/test_conf.ini'))
        return dict(config.items(item))


    def pase_element_find_method(self,str):
        list=str.split('>')
        spetator=list[0]
        value =list[1]
        return spetator,value

    def contain_str(self,str1,str2):
        return string.find(str1,str2)

    def get_all_table_element_xpath(self,item,key,table_xpath_locator=None):
        table_xpath_locator=item.get(key)
        xpath=[]
        for i in range(1,7):
            for j in range(1,7):
                msg=table_xpath_locator+"tr["+str(i)+"]/td["+str(j)+"]"
                xpath.append(msg)
        return  xpath




if __name__ =="__main__":
    item=Constant().Read_file_init('index')
    for i in range(1,6):
        print item.get("index_newfishs"+str(i))
    str3="传统融资遇困境，大象钢票“吉象三保”解"
    str1="传统融资遇困境，大象钢票“吉象三保”解困难"
    print Constant().contain_str(str1,str3)
    print Constant().get_all_table_element_xpath(item,'index_steel_recommd_link_table')