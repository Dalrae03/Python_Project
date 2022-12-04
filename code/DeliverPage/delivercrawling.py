import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re  #정규 표현식 불러오기
import random
from tqdm import tqdm
from collections import defaultdict
import json
import pandas as pd


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()
browser.get("https://www.yogiyo.co.kr/mobile/#/")
# 요기요 검색창으로이동


elem = browser.find_element("name", "address_input")
elem.clear()
time.sleep(1)
que = "세종특별자치시 조치원읍 신안리 300 홍익대학교세종캠퍼스" #검색어 입력
elem.send_keys(que)
elem.send_keys(Keys.ENTER)
time.sleep(1)
#입력까진 완료인데 버튼이 안눌린다... 대가리 터질것같다...
# browser.find_element("xpath", "//*[@id='search']/div/form/ul[2]/li[3]/a").click() <- 오류남
browser.find_element("xpath", '//*[@id="search"]/div/form/ul/li[3]/a').click()
time.sleep(1)

List = browser.find_element("xpath", '//*[@id="content"]/div/div[4]/div/div[2]').find_elements("class name", "col-sm-6")





# for li in list:
#   print(li.find_element("class name", "item clearfix").text)




# print(browser.find_element("xpath", '//*[@id="content"]/div/div[2]/div/div[2]/div[2]/div')) -> 프린트는 되는 것 같다

# browser.find_element("class name", "btn btn-default ico-pick").click()
# time.sleep(2)

# browser.find_element("class name", "form-control ng-pristine ng-valid ng-scope ng-valid-required ng-valid-minlength ng-touched").click()

# browser.find_elements("class name", "restaurants-info")

# print(url)

'''
Menu = []
Menu.append(browser.find_elements("class name", "item clearfix"))  #가게 박스를 리스트로 넣어버림
print(Menu)
'''
# pick = random.choice(Menu)
# print(pick)


'''
res = requests.get(browser)  #브라우저 링크 수정해야함
#우리지역에 해당하는 가게 모음 요기요링크
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")  #BeautifulSoup 객체 만들기
'''


# 가게이름 최소주문금액 배달비 평점 <- 뽑아야할 것
# 랜덤으로 고른 가게의 이름과 동일한 요소의 정보들을 뽑아야함 <- 수정요함
'''
  #가게이름
  #최소주문금액
#배달비
 #평점
'''


# 저 마지막이 끝나고나서 창이 사라저 버림 -> 함수가 종료되고 나서 크롬드라이버는 사라져버림 작동은 된다
# 네이버 로그인 셀레니움
'''
browser.get("https://www.naver.com/")
elem =browser.find_element("class name", "link_login") 
elem.click()

browser.find_element("id", "id").send_keys("www298")
browser.find_element("id", "pw").send_keys("yejin1020")

browser.find_element("class name", "btn_login").click()
'''





# inform = browser.find_elements("class", "restaurants-info") 셀레니움 말고 수프 써야하는거 아님?


'''
res = requests.get(browser)
#우리지역에 해당하는 가게 모음 요기요링크
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  #BeautifulSoup 객체 만들기

Menu = []


stname = soup.find_all("div", attrs = {"class":"restaurants-info"})  #여기서부터 싹다 수정하기...
print('식당 수:', len(stname))


for i, stname in enumerate(stname):
    if i == 15:
        break
    print(stname.get_text())
'''