import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.yogiyo.co.kr/mobile/#/%EC%84%B8%EC%A2%85%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EC%8B%9C/000000/')
#우리지역에 해당하는 가게 모음 요기요링크
page.raise_for_status()

soup = BeautifulSoup(page.text, "lxml")  #BeautifulSoup 객체 만들기

Menu = []

stname = soup.find("div", attrs = {"class":"restaurants-info"})  #여기서부터 싹다 수정하기...
print("stname: {}".format(stname.div.get_text()))
