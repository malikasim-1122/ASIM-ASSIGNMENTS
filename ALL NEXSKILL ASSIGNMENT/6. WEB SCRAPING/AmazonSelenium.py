from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

cService = webdriver.ChromeService(executable_path="C:\\Users\\LAYYAH LAPTOPS\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=cService)

driver.get(url)

homelist =[]
homeDiv = driver.find_elements(By.XPATH,"//li[contains(@class,'a-carousel-card ucw-widget-carousel-element')]")
for h in range(len(homeDiv) -1) :
    home ={}
    innerImg = homeDiv[h+1].find_element(By.TAG_NAME,"img")
    innera = homeDiv[h+1].find_element(By.TAG_NAME,"a")
    home["img"] = innerImg.get_attribute("src")
    home["lines"] = innerImg.get_attribute("alt")
    home["url"] = innera.get_attribute("href")
    homelist.append(home)
filename = 'Amazone_Home_Sale.csv'
with open(filename,'w',newline='') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for home in homelist:
        w.writerow(home)
driver.close