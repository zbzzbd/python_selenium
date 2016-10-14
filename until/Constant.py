# -*- coding:utf-8 -*-
import ConfigParser
import os

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

if __name__ =="__main__":
    item=Constant().Read_file_init('index')
    for i in range(1,6):
        print item.get("index_newfishs"+str(i))