import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()


browser.get("https://www.yogiyo.co.kr/mobile/#/")
# 요기요 검색창으로이동

elem = browser.find_element("name", "address_input")

que = "세종특별자치시 조치원읍 신안리 300 홍익대학교세종캠퍼스" #검색어 입력
elem.send_keys(que)

elem.send_keys(Keys.ENTER)

print(browser.find_elements("class name", "restaurants-info"))




# 저 마지막이 끝나고나서 창이 사라저 버림 -> 함수가 종료되고 나서 크롬드라이버는 사라져버림 작동은 된다
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