#-*-coding:utf-8 -*-
from PageObject.base import GG_BasePage

class PersonalModifyInfo(GG_BasePage):
    """
    1.从配置文件中读取其中的配置，
    2.根据读取的配置调用解析方法进行定位元素
    3.封装各种操作的方法
    4.验证操作的正确性
    """
    def __init__(self,driver):
        self.driver =driver
        self.item=self._get_element_position('mycenter_personal_information')

    def _get_element_position(self,module):
        item = self.Read_elements_item(module)

        self.personal_link=item.get('personal_link')
        self.name=item.get('name')
        self.sex=item.get('sex')
        self.company=item.get('company')
        self.Province=item.get('address_province')
        self.city=item.get('address_city')
        self.area=item.get('address_area')
        self.detail=item.get('address_detail')
        self.mobile=item.get('mobile')
        self.qq = item.get('qq')
        self.businessScope = item.get('business_scope')
        self.submit = item.get('submit')
        self.canel = item.get('button_canel')
        return item

    #点击个人信息链接
    def click_personal_info_link(self):
        self._click_element(self.personal_link)

    #输入姓名
    def send_username(self,newname):
        self._input_text(self.name,newname)

    #输入公司名称
    def send_companyName(self,company_name):
        self._input_text(self.company,company_name)


    #设置性别
    def click_sex_Radio_button(self,value_sex):
        #拼接定位value_sex  value="男" 或者 value="女"
        find_type,value_used=self._locaotor_value_join(self.sex,value_sex)

        element=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value_used))
        element.click()

    #点击保存按钮
    def click_save_button(self):
        self._click_element(self.submit)

    #修改个人信息方法
    def modify_personal_info(self,username,sex,company_name):
        self.send_username(username)
        self.send_companyName(company_name)
        self.click_sex_Radio_button(sex)
        self.click_save_button()









