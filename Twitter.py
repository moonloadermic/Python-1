from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time
import re
from datetime import datetime
from pyvirtualdisplay import Display


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



url = "https://twitter.com/whyyoutouzhele"
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(6)

end_time = time.time() + 35
while time.time() < end_time:
    driver.execute_script("window.scrollBy(0, 40);")
    time.sleep(0.5)

html = driver.page_source
print(html)
exit()

