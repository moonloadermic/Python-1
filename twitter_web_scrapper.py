from selenium import webdriver
from selenium.webdriver.common.by import By
import time,webbrowser
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import sys

display = Display(visible=0, size=(1920, 1080))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--enable-javascript') # 启用 JavaScript
options.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
options.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
options.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')           # 隐藏滚动条，应对一些特殊页面
options.add_argument("--headless") #无界面


driver = webdriver.Chrome(options=options)
userName = sys.argv[1]
driver.get(f"https://twitter.com/{userName}")
	
	
'''處理可能出現的失效頁面：'''
try:
		driver.find_element(By.XPATH,"//a[@id='button_retry']")
		driver.find_element(By.XPATH,"//a[@id='button_retry']").click()
		time.sleep(5)
except:pass

time.sleep(5)
driver.switch_to.window(driver.window_handles[-1]) #将 Selenium WebDriver 的焦点切换到当前窗口的最后一个句柄（即最后一个打开的标签页或窗口
driver.find_element(By.XPATH,'//body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,'//body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.XPATH,'//body').send_keys(Keys.PAGE_DOWN)
time.sleep(1)


elementDate=driver.find_elements(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div/div/div/article/div/div/div[2]/div[2]/div[2]")
elementUrl=driver.find_elements(By.XPATH,"//*[contains(@id,'id')]/div[2]/div/div[3]/a")
with open('twitter.html','a+')as file:
	for i in range(5):
		content=elementDate[i].text+'|'+elementUrl[i].get_attribute('href')
		print(content)
