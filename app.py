from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/sresults', methods=['POST'])

def searching():
   keyword_receive = request.form['keyword_give']
   response = requests.get("https://openapi.naver.com/v1/search/shop.json",
                           params={"query": keyword_receive, "display": 1},
                           headers={"X-Naver-Client-Id": "3T2wQJ3_WgsPtjM1hqgp", "X-Naver-Client-Secret": "BrHLav3UBB"})

   print(response.status_code)
   return jsonify({'result':'success', 'msg': '검색이 완료되었습니다', 'items': response.json()['items']})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)