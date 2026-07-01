from selenium.webdriver.common.by import By
#进入界面的登录元素
Enter=(By.XPATH,"//*[@id='app']/div[1]/form/div[3]/div/button")
#系统管理元素
click_systemm=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div")
#用户管理
click_userm=(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li/span")
#新增按钮
click_addUser=(By.XPATH,"//*[@id='app']/div[1]/div[2]/section/div/div[2]/div/div[1]/div[1]/button")
#用户昵称元素
UserId=(By.XPATH,"//input[contains(@placeholder,'请输入用户昵称')]")
#手机号元素
PhoneNumber=(By.XPATH,"//div[contains(@class,'el-input--medium')]//input[contains(@placeholder,'请输入手机号码')]")
#用户名称元素
UserName=(By.XPATH,"//div[contains(@class,'el-input--medium')]//input[contains(@placeholder,'请输入用户名称')]")
#邮箱元素
PostId=(By.XPATH,"//input[contains(@placeholder,'请输入邮箱')]")
#点击岗位元素的下拉
Occuptionset=(By.XPATH,"//div[contains(@class,'el-select')]//input[@placeholder='请选择岗位']/ancestor::div[contains(@class,'el-select')]")
#岗位元素
Occuption=(By.XPATH,"//div[contains(@class,'el-select-dropdown')]//span[text()='董事长']")
#点击用户性别
Click_Gender=(By.XPATH,"//input[contains(@placeholder,'请选择性别')]/ancestor::div[contains(@class,'el-select')]")
#选择用户性别
Gender=(By.XPATH,"//div[contains(@class,'el-select-dropdown__wrap')]//li[contains(@class,'el-select-dropdown__item')]//span[text()='女']")
#点击角色元素
Click_Character=(By.XPATH,"//input[@placeholder='请选择角色']/ancestor::div[contains(@class,'el-select')]")
#选择角色元素
Character=(By.XPATH,"//div[contains(@class,'el-select-dropdown__wrap')]//span[text()='普通角色']")
#点击部门元素
Click_partment=(By.XPATH,"//input[@class='vue-treeselect__input']/ancestor::div[contains(@class,'vue-treeselect__control')]")
#选择部门
partment=(By.XPATH,"//div[contains(@class,'vue-treeselect__label-container')]//label[contains(text(),'若依科技')]")
#确定按钮元素
Ensure=(By.CSS_SELECTOR,"body > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary.el-button--medium > span")

#验证用户已存在
Adduser_success=(By.XPATH,"//p[@class='el-message__content']")

#用户昵称不能为空
UserName_notNull=(By.XPATH,"//div[@class='el-form-item__error']")

