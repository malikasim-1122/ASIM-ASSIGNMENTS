from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
cService = webdriver.ChromeService(executable_path="C:\\Users\\LAYYAH LAPTOPS\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=cService)
driver.get(url)

phonelist =[]
phoneDiv = driver.find_elements(By.XPATH,"//div[contains(@class,'Bm3ON')]")
for p in range(len(phoneDiv) -1):
    phone = {}
    innerImg = phoneDiv[p+1].find_element(By.TAG_NAME,"img")
    innera = phoneDiv[p+1].find_element(By.TAG_NAME,"a")
    phone["img"] = innerImg.get_attribute('src')
    phone["lines"] = innerImg.get_attribute('alt')
    phone["url"] = innera.get_attribute('href')
    phonelist.append(phone)
filename = 'Daraz_Product.csv'
with open(filename,'w',newline='') as f:
     w = csv.DictWriter(f,['url','img','lines','auther'])
     w.writeheader()
     for phone in phonelist:
          w.writerow(phone)
driver.close