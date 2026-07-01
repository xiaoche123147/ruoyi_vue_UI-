import logging
import time
import unittest
from time import sleep

import allure
import pytest
from base.GetDriver import Getdriver
from page.add_user import Add_User
from base.logs import log


class Mytestcase(unittest.TestCase):
    driver = None

    @pytest.fixture(autouse=True)
    def server(self):
        self.driver = Getdriver().Get_driver()
        self.adduser = Add_User(self.driver)
        log.info("浏览器启动")
        yield
        Getdriver().quit_driver()
        log.info("退出浏览器")

    # @pytest.mark.parametrize("ID,Phone,UserName,Post2",
    #                          [],
    #                          [],
    #                          [])
    # 正向测试
    @allure.title("正确的用户信息登录成功")
    def test01_right(self):
        self.adduser.enter()
        time.sleep(3)
        self.adduser.enter_Systemm()
        time.sleep(3)
        self.adduser.Click_AddUser()
        time.sleep(3)
        self.adduser.Add_User()
        time.sleep(3)
        self.adduser.Click_userId("11")
        time.sleep(3)
        self.adduser.send_Phone("13723551068")
        time.sleep(3)
        self.adduser.click_addUser("xiaochen")
        time.sleep(3)
        self.adduser.select_gender()
        time.sleep(3)
        self.adduser.select_post()
        time.sleep(3)
        self.adduser.select_role()
        time.sleep(3)
        self.adduser.self_parment()
        time.sleep(3)
        self.adduser.click_post("1826115142@qq.com")
        time.sleep(3)
        self.adduser.click_ensure()

    # 反向新增用户测试
    def test02(self):
        self.adduser.enter()
        time.sleep(3)
        self.adduser.enter_Systemm()
        time.sleep(3)
        self.adduser.Click_AddUser()
        time.sleep(3)
        self.adduser.Add_User()
        time.sleep(3)
        self.adduser.Click_userId("15")
        time.sleep(3)
        self.adduser.send_Phone("13723551069")
        time.sleep(3)
        self.adduser.click_addUser("xiaochen")
        time.sleep(3)
        self.adduser.select_gender()
        time.sleep(3)
        self.adduser.select_post()
        time.sleep(3)
        self.adduser.select_role()
        time.sleep(3)
        self.adduser.self_parment()
        time.sleep(3)
        self.adduser.click_post("1826115142@qq.com")
        time.sleep(3)
        self.adduser.click_ensure()
        try:
            ex = self.adduser.exist_user()
            lizi = "登录账号已存在"
            assert lizi in ex, f"注册用户出现异常预期出现{lizi},实际出现{ex}"
            log.info("反向测试通过")
        except (TimeoutError,AssertionError) as e:
            path_url = self.adduser.Save_screenshot()
            log.error(f"出现意料之外的注册用户误差{str(e)}，截图路径为{path_url}", exc_info=True)
            raise