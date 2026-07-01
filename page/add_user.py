import time
from csv import excel
from sys import exc_info
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from base.logs import log
import page


class Add_User(Base):
    # 点击登入
    def enter(self):
        self.click_element(page.Enter)
        log.info("我点击登录了")

    # 点击系统管理
    def enter_Systemm(self):
        self.click_element(page.click_systemm)
        log.info("点击系统管理")
        time.sleep(3)
        # 点击用户管理

    def Click_AddUser(self):
        self.click_element(page.click_userm)
        log.info("点击了用户管理")

        # 点击新增用户

    def Add_User(self):
        self.wait_click_element(page.click_addUser)
        log.info("点击新增用户")

        # 点击输入用户昵称并输入昵称

    def Click_userId(self, ID):
        self.send_keys(page.UserId, ID)
        log.info("点击用户昵称并输入昵称")

        # 点击输入手机号码

    def send_Phone(self, Phone):
        self.send_keys(page.PhoneNumber, Phone)
        log.info("点击输入手机号码")

        # 点击输入用户名称

    def click_addUser(self, UserName):
        self.send_keys(page.UserName, UserName)
        log.info("点击用户名称")

        # 点击输入性别

    def select_gender(self):
        self.wait_click_element(page.Click_Gender)
        log.info("点击性别下拉框")
        self.wait_click_element(page.Gender)
        log.info("选中性别")

        # 点击选择职位

    def select_post(self):
        self.wait_click_element(page.Occuptionset)
        log.info("点击职位元素下拉框")
        self.wait_click_element(page.Occuption)
        log.info("选中职位")

        # 选择角色

    def select_role(self):
        self.wait_click_element(page.Click_Character)
        log.info("点击选择角色下拉框")
        time.sleep(2)
        self.wait_click_element(page.Character)
        log.info("选中对应的角色")

        # 输入部门

    def self_parment(self):
        self.wait_click_element(page.Click_partment)
        log.info("选中部门下拉框")
        time.sleep(2)
        self.wait_click_element(page.partment)
        log.info("选中对应的部门")

        # 点击输入邮箱

    def click_post(self, Post2):
        self.send_keys(page.PostId, Post2)
        log.info("输入对应的邮箱号")

        # 点击确认

    def click_ensure(self):
        self.wait_click_element(page.Ensure)
        log.info("点击确认按钮")
        #验证用户已存在反例
    def exist_user(self):
        user_text=self.element(page.Adduser_success).text
        return user_text