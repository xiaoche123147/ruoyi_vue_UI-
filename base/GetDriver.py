from selenium import webdriver
class Getdriver:
    driver = None
    #获取浏览器
    @classmethod
    def Get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            #浏览器最大化
            cls.driver.maximize_window()
            #等待10s
            cls.driver.implicitly_wait(10)
            #打开浏览器页面
            cls.driver.get(" http://localhost:80/")
        return cls.driver
    #关闭浏览器
    @classmethod
    def quit_driver(cls):
        #关闭浏览器
        cls.driver.quit()
        cls.driver=None