from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from tqdm import tqdm
from collections import defaultdict
import pandas as pd


browser = webdriver.Chrome()
browser.get("https://www.yogiyo.co.kr/mobile/#/")
# 요기요로 이동


elem = browser.find_element("name", "address_input")  #요기요 검색창 찾기
elem.clear()  #기본적으로 입력되는것 지워주기
time.sleep(1) #종종 1초 쉬어주기
que = "세종특별자치시 조치원읍 신안리 300 홍익대학교세종캠퍼스"  #검색어 입력
elem.send_keys(que)
elem.send_keys(Keys.ENTER)
time.sleep(1)
browser.find_element("xpath", '//*[@id="search"]/div/form/ul/li[3]/a').click() #검색후 엔터한번 치고 검색창 밑에 뜨는 똑같은 주소 클릭하기
time.sleep(1)

List = browser.find_element("xpath", '//*[@id="content"]/div/div[4]/div/div[2]').find_elements("class name", "col-sm-6") 
#요기요 등록 음식점에 있는 음식점들(정보상자) 리스트 만들기

Menu = []

for li in List:
  if(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("class") == "logo"):  #리스트 전부 돌며 현재 영업안하는 음식점 걸러내기
    Menu.append(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("style"))  #음식점들 사진 리스트 만들기

  else:
    pass

# print(Menu)

ch = random.choice(Menu)  #안의 사진주소들 모두 문자열 취급 / 사진리스트 중 하나 랜덤뽑기
# print(ch)

for li in List:  #뽑은 사진과 동일한 요소를 가지고있는 가게 정보상자 찾기
  if(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("style") == ch): 
    Site = li.find_element("tag name", "div")

  else:
    pass

Site.click()  #정보 상자 클릭하기
time.sleep(3)


# 가게이름 최소주문금액 배달비 평점 <- 뽑아야할 것
# 랜덤으로 고른 가게의 이름과 동일한 요소의 정보들을 뽑아야함

Info = browser.find_element("class name", "col-sm-8").find_element("class name", "restaurant-info")
Dliever = browser.find_element("tag name", "ng-include").find_element("tag name", "div")

print(Info.find_element("class name", "restaurant-title").find_element("tag name", "span").text)  #가게이름 
print(Info.find_element("class name", "restaurant-content").find_element("tag name", "ul").find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/span').text)
#최소 주문금액
print(Dliever.find_element("class name", "cart").find_element("class name", "clearfix").find_element("tag name", "span").text)  #배달비
print(Info.find_element("class name", "restaurant-content").find_element("tag name", "ul").find_element("tag name", "span").text)  #평점

