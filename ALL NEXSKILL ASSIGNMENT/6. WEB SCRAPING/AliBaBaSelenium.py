from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import csv

url = "https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all"

cService = webdriver.ChromeService(executable_path="C:\\Users\\LAYYAH LAPTOPS\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=cService)
wait = WebDriverWait(driver,10)
driver.get(url)

productlist = []
productDiv = driver.find_elements(By.XPATH,"//div[contains(@class,'_67cIk073 creative-product-card C-QiDMGT')]")
for p in range(len(productDiv) -1):
    product = {}
    innerImg = productDiv[p+1].find_element(By.TAG_NAME,"img")
    innera = productDiv[p+1].find_element(By.TAG_NAME,"a")
    product["img"] = innerImg.get_attribute("src")
    product["lines"] = innerImg.get_attribute("alt")
    product["url"] = innera.get_attribute("href")
    productlist.append(product)
filename = 'AliBaBa_Product.csv'
with open(filename,'w',newline='') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for product in productlist:
        w.writerow(product)
driver.close