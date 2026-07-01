from datetime import datetime
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.logs import log


class Base:
    # 元素初始化
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #等待
    def element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    # 点击元素
    def click_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).click()

    # 用于等待元素可以被点击
    def wait_click_element(self, locator):
        wait_control = self.wait.until(EC.element_to_be_clickable(locator))
        wait_control.click()
        time.sleep(1)

    # 输入文本
    def send_keys(self, locator, key):
        send_keya = self.wait.until(EC.element_to_be_clickable(locator))
        send_keya.clear()
        send_keya.send_keys(key)

    # 写入错误截图
    def Save_screenshot(self):
        screenshot_path = os.path.join(os.getcwd(), 'screenshot')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        file_name = datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        file_path = os.path.join(screenshot_path, file_name)
        self.driver.save_screenshot(file_path)
        return file_path

    # 用于判断文本断言是否符合

    def check_text(self, locator, excepted_text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator)).text
            assert excepted_text == element, f"预期文本{excepted_text},实际文本{element} 断言失败"
            log.info("断言用例通过")
        except AssertionError as e:
            path_url=self.Save_screenshot()
            log.error(f"断言不通过 报错信息{str(e)}，截图路径为{path_url}",exc_info=True)
            raise
