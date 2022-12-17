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

photo_url = ch[23:-45]  #사진 링크 필요부분만 잘라내기
print(photo_url)

# print(ch)

for li in List:  #뽑은 사진과 동일한 요소를 가지고있는 가게 정보상자 찾기
  if(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("style") == ch): 
    Site = li.find_element("tag name", "div")
    break

  else:
    pass

Site.click()  #정보 상자 클릭하기
time.sleep(1)


# 가게이름 최소주문금액 배달비 평점 <- 뽑아야할 것
# 랜덤으로 고른 가게의 이름과 동일한 요소의 정보들을 뽑아야함

Dliver_Date = []

Dliver_Date.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/span').text)  #가게이름 
Dliver_Date.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/span').text)  #최소 주문금액
Dliver_Date.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[2]/ng-include/div/div[2]/div[4]/span[1]').text)  #배달비
Dliver_Date.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/span').text)  #평점


print(Dliver_Date)

# 과정 알고리즘
'''
1. 요기요 창 이동
2. 검색창을 찾아 클릭 후 적혀있는 현재 주소 지운 뒤 원하는 주소 입력 후 엔터
3. 연관검색어 중 같은 내용의 선택지 클릭
4. 등록 음식점 란에 있는 모든 가게들 요소 추출하기
5. 반복문을 통해 현재 영업하지않는 가게들을 걸러 메뉴리스트에 가게이미지링크 넣기
6. 랜덤함수를 통해 가게이미지 링크 하나 랜덤 추출
7. 모든 가게들이 가지고 있는 요소중 랜덤으로 나온 가게이미지요소를 가지고있는 가게 추출
8. 추출한 것 클릭
9. 가게정보들이 묶여있는 요소를 가르키는 변수와 배달비를 포함하고있는 요소를 가르키는 변수 설정
10. 가게 정보들이 묶여있는 요소를 가르키는 변수사용하여 가게이름, 최소 주문금액, 평점 글씨 출력
11. 배달비를 포함하고있는 요소를 가르키는 변수를 사용하여 배달비 출력
'''