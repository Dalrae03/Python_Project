from flask import Flask,render_template,jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import random

# ---------------------------------------------------------------------------------------------------------------------- 내꺼 최종수정 완
#셀레니움 크롤시에 에 창이 뜨지 않게 해줍니다.
options = webdriver.ChromeOptions()
options.add_argument("headless")

#요기요 크롤링 코드입니다.
def get_deliver():
  browser = webdriver.Chrome(options=options)
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
  #요기요 등록 음식점에 있는 음식점들(정보상자) 변수만들기

  Menu = []

  for li in List:
    if(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("class") == "logo"):  
      #리스트 전부 돌며 현재 영업안하는 음식점 걸러내기
      Menu.append(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("style"))  #음식점들 사진정보 리스트 만들기

    else:
      pass

  # print(Menu)
  ch  = random.choice(Menu)  #안의 사진주소들 모두 문자열 취급 / 사진정보리스트 중 하나 랜덤뽑기
  photo_url = ch[23:-45]  #사진을 사용하기위해 사진이 담겨있는 url앞뒤로 불필요한 정보들을 리스트 인덱싱으로 잘라버리기
  # print(ch)

  for li in List:  #뽑은 사진정보과 동일한 요소를 가지고있는 가게 정보상자 찾기
    if(li.find_element("tag name", "td").find_element("tag name", "div").get_attribute("style") == ch): 
      Site = li.find_element("tag name", "div")
      break

    else:
      pass

  Site.click()  #정보 상자 클릭하기
  time.sleep(1)



  # 가게이름 최소주문금액 배달비 평점 <- 뽑아야할 것
  # 랜덤으로 고른 가게의 이름과 동일한 요소의 정보들을 뽑아야함

  Deliver_Data = []

  current_URL = browser.current_url # current_URL에 현재 페이지의 url을 집어 넣음

  Deliver_Data.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/span').text)  #가게이름 
  Deliver_Data.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/span').text)  #최소 주문금액
  Deliver_Data.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[2]/ng-include/div/div[2]/div[4]/span[1]').text)  #배달비
  Deliver_Data.append(browser.find_element("xpath", '//*[@id="content"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/span').text)  #평점

  Deliver_Data.append(current_URL) #현재 url 추가 함
  Deliver_Data.append(photo_url)


  return Deliver_Data

# --------------------------------------------------------------------------------------------------------------------------------------


#포장 추천 페이지 관련 코드
# 카카오 api의 키워드 검색 기능
url = "https://dapi.kakao.com//v2/local/search/keyword.json"  

#api 요청자 정보 KakaoAk 뒤에 본인의 카카오 Reset Api 키 입력
headers = {"Authorization": "KakaoAK enter your kakao api key"}

#전체 정보를 담아옵니다. 
total = []

is_last = False
i = 1
#마지막 페이지까지 반복
while is_last == False:

    #파라미터를 담습니다 query = 검색할 키워드(문자열),  x : 중심 경도(문자열), y: 중심 위도(문자열). radius : 반경 설정(정수형)(현재 반경 600미터), category_group_code : 카카오맵 분류 코드(문자열)(현재는 식당코드), page : i(정수)
    params = {'query' : "홍익대학교 세종캠퍼스 식당", 'x' : "127.28461813707062", 'y' : "36.6196348237162", 'radius' : 600, 'category_group_code' : 'FD6', 'page' : i } 

    #위의 파라미터를 기준으로 페이지의 식당 정보를 json형태로 출력
    places = requests.get(url, params=params, headers=headers).json()

    #총 식당 정보 리스트에 현재 페이지의 리스트를 추가
    total.append(places)
    i += 1

    #현재 페이지가 마지막 페이지인지 반환 마지막 페이지면 : True, 그렇제 않으면 False
    is_last = requests.get(url, params=params, headers=headers).json()['meta']['is_end']

#추출된 여러 가게 들중에서 하나의 가게만을 추천해주는 코드입니다.
def recommend():
    # 페이지 수
    total_pages = len(total)

    #랜덤한 페이지를 choosed_Page에 저장
    random_pgNum = random.randrange(0, total_pages)
    choosed_Page = total[random_pgNum]

    #랜덤 선택된 페이지의 가게 정보들만을 choosed_Stores에 저장  => 뒤에 붙은 meta 정보 제거
    choosed_Stores = choosed_Page["documents"]

    #선택된 페이지의 가게 수들을 저장
    StoreNum = len(choosed_Stores)

    #랜덤으로 n번째 가게 추출
    random_StoreNum = random.randrange(0,StoreNum)
    random_StoreInfo = choosed_Stores[random_StoreNum]

    dict = {"StoreInfo" :random_StoreInfo}
    return dict

recom_data = dict

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


#mainPage-router
@app.route('/')
def mainPage():
    return render_template('index.html')

#packagePage-router
@app.route('/package')
def packagepage():
    return render_template('package.html')

#deliverPage-router
@app.route('/deliver')
def deliverpage():
    return render_template('deliver.html')

#mapPage-router
@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/packagedata')
def get_package_data():
    data = recommend()
    return jsonify(data)

@app.route('/deliverdata')
def get_deliver_data():
    random_deliver = get_deliver()
    return jsonify(random_deliver)

#5001번 포트, 디버그 모드로 실행(서비스시 지울것)
app.run(port = 5001, debug = True)