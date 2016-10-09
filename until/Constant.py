# -*- coding:utf-8 -*-
import ConfigParser

"""
常用的方法
"""
class Constant(object):

    def Read_file_init(self,item):
        config = ConfigParser.ConfigParser()
        config.readfp(open('D:\\code\\dx_py_auto_selenium\\element.ini'))
        #print config.items(item)
        return dict(config.items(item))

    def pase_element_find_method(self,str):
        list=str.split('>')
        spetator=list[0]
        value =list[1]
        return spetator,value

if __name__ =="__main__":
    item=Constant().Read_file_init('login')
    print item.get('username')