# -*- coding:utf-8 -*-
from .base import GG_BasePage
from until.Constant import Constant
import time
class IndexPageObject(GG_BasePage):
    def __init__(self,driver):
        self.driver=driver
        self.item=self._get_elements_position('index')

    def _get_elements_position(self,module_item):
        item =self.Read_elements_item(module_item)
        self.spot_good=item.get('spot_goods')
        self.ticket =item.get('apply_tikcet')
        self.mycenter=item.get('mycenter')
        self.structral_steel=item.get('index_banner_structral_steel')
        return item
    #点击去找货
    def click_spotGood_button(self):
        find_type,value = self.get_type_locator(self.spot_good)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()
    #点击申请钢票贷
    def click_apply_ticket(self):
        find_type,value = self.get_type_locator(self.ticket)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()

    #鼠标移动到
    def move_structral_steel(self):
        find_type,value=self.get_type_locator(self.structral_steel)
        element=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
        self.mouse_on_element(element)
        time.sleep(2)

    #点击首页轮播图旁边的菜单
    def click_index_banner_link(self):
        find_type,value=self.get_type_locator(self.item)
        element=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
        element.click()


    #批量点击轮播图旁边的菜单的二级菜单
    def click_index_bannner_links(self):
        for i in range(1,11):
            #鼠标悬浮钢材库
            self.move_structral_steel()
            #点击队应的元素
            find_type,value=self.get_type_locator(self.item.get("index_banner_structral_steel_node_"+str(i)))
            print i,find_type,value
            self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()
            #检验是否进入相应的页面
            main_window=self.is_into_sheelPage_succed()
            #关闭当前页面
            self.driver.close()
            #切换到主窗口
            self.switch_main_window(main_window)

    #批量点击钢铁推荐的表格
    def click_index_recommd_table(self):
        xpath_link=Constant().get_all_table_element_xpath(self.item,"index_steel_recommd_link_table")
        for path in xpath_link:
            find_type,value=self.get_type_locator(path)
            self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
            #检查是否进入四方现货页面
            main_window=self.is_spod_successd()
            self.driver.close()
            self.switch_main_window(main_window)



    #判断当前是否登录状态
    def is_logined(self):
        flage=None
        cookies=self.get_cookiesValue_by_name(self.driver,"token")
        print cookies

        if cookies is not None:
            print "登录成功"
            flage=True
            return flage
        return flage

    # 点击我的钢钢网
    def click_into_my_center(self):
        find_type,value=self.get_type_locator(self.mycenter)
        self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value)).click()

    #点击钢钢快报链接
    def click_and_verfity_newflashes(self):
        #获取定位方式
        for i in range(1,6):
            link=self.item.get("index_newfishs"+str(i))
            find_type,value =self.get_type_locator(link)
            link_element=self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
            # 点击并获取其属性href
            #link_href=link_element.get_attribute('href')
            link_text=link_element.text
            #点击链接
            link_element.click()
            self.is_goto_newPage(link_text)

    def click_and_verify_steel_img(self):
        for i in range(1,11):

            str1="index_steel_recommd_img_"+str(i)
            print str1
            img = self.item.get("index_steel_recommd_img_"+str(i))
            print img
            find_type,value = self.get_type_locator(img)
            img_el = self.wait_until_element(self.driver,self.according_type_switch_method(find_type,value))
            img_el.click()
            main_window=self.is_into_sheelPage_succed()
            self.driver.close()
            self.switch_main_window(main_window)

    #封装验证是否成功跳入四方现货页面
    def is_spod_successd(self):
        #1.转化窗口
        main_window =self.switch_window()
        #获取窗口标题
        title = self.driver.title
        print title
        assert  title.encode("utf-8").startswith('钢钢网-四方现货')
        return main_window
    #封装是否成功跳入钢钢网页面
    def is_apply_ticket_successd(self):
        self.switch_window()
        title = self.driver.title
        assert  title.encode("utf-8").startswith('钢钢网-大象钢票')

    #封装是否成功进入个人中心
    def is_into_mycenter_succesd(self):
        self.switch_window()
        title = self.driver.title
        assert  title.encode("utf-8").startswith('钢钢网-会员中心')

    def is_into_sheelPage_succed(self):
        mainwindow=self.switch_window()
        title= self.driver.title
        assert title.encode("utf-8").startswith('钢钢网-钢材库')
        return mainwindow
    #封装验证链接是否进入的相应的页面
    def is_goto_newPage(self,text):
        #1. title 包含文字内容
        #2. 关闭链接窗口，切换到主窗口
        main_window=self.switch_window()
        title= self.driver.title
        if Constant().contain_str(title.encode("utf-8"),text.encode("utf-8"))==0:
            self.driver.close()
            self.switch_main_window(main_window)

