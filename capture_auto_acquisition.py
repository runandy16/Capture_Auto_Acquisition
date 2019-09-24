import time
import re
from selenium import webdriver
from PIL import Image, ImageChops

urls = open("/Capture_Auto_Acquisition/キャプチャ自動取得/キャプチャページURL.txt", "r",encoding="Shift_JIS")
names = open("/Capture_Auto_Acquisition/キャプチャ自動取得/キャプチャ保存名.txt", "r",encoding="Shift_JIS")

data_dic = {name.replace('\n','') : url.replace('\n','') for name, url in zip(names, urls)}
　
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

for name, url in data_dic.items():
  driver.get(url)
  height = driver.execute_script("return document.body.scrollHeight;")
  driver.set_window_size(1250, height)

  # 読み込み待機時間
  time.sleep(2)
  driver.save_screenshot(f"/Capture_Auto_Acquisition/キャプチャ自動取得/{name}.png")

# プラウザを閉じる
driver.quit()
