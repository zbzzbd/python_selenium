# -*- coding:utf-8 -*-
import ConfigParser
import os
import  string
import xlrd

"""
常用的方法
"""
class Constant(object):
    def __init__(self):
        #根目录
        self.file_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.filename=self.Read_file_config('file').get('filename')
        self.xls_filename=self.Read_file_config('file').get('xlsfilename')



    def Read_file_init(self,item):

        config = ConfigParser.ConfigParser()
        config.readfp(open(self.file_dir+'/'+self.filename))

        return dict(config.items(item))

    def Read_file_config(self,item):

        config = ConfigParser.ConfigParser()
        config.readfp(open(self.file_dir + '/test_conf.ini'))
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

    #本方法仅供读取xls文件，因为xlrd此包不支持xlsx.
    def Read_excel(self,table_name):
        data = xlrd.open_workbook(self.file_dir+'/'+self.xls_filename)
        print data.sheet_names()[0].encode('utf-8')
        #获取第一个修改密码的表格
        table=data.sheet_by_name(table_name.decode('utf-8'))
        rows=table.nrows
        cols=table.ncols
        arr=[]
        for i in range(rows):
            if i==0:
                continue
            arr.append(table.row_values(i)[:])
        print arr



if __name__ =="__main__":
    """item=Constant().Read_file_init('index')
    for i in range(1,6):
        print item.get("index_newfishs"+str(i))
    str3="传统融资遇困境，大象钢票“吉象三保”解"
    str1="传统融资遇困境，大象钢票“吉象三保”解困难"
    print Constant().contain_str(str1,str3)
    print Constant().get_all_table_element_xpath(item,'index_steel_recommd_link_table')
    """
    print Constant().Read_excel("修改密码")