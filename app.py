from flask import Flask, render_template, jsonify, request, Response
import pandas as pd
from io import StringIO
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

@app.route('/json2csv', methods=['POST'])
def json2csv():
    data = request.get_json(force=True)
    print(type(data))
    #df = pd.read_json(data) 
    df = pd.DataFrame(data)

    output = StringIO()
    output.write(u'\ufeff') # 한글 인코딩 위해 UTF-8 with BOM 설정해주기
    df.to_csv(output)
    # CSV 파일 형태로 브라우저가 파일다운로드라고 인식하도록 만들어주기
    response = Response(
        output.getvalue(),
        mimetype="text/csv",
        content_type='application/vnd.ms-excel',
        #content_type='application/octet-stream',
    )
    response.headers["Content-Disposition"] = "attachment; filename=download.csv" # 다운받았을때의 파일 이름 지정해주기
    return response

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
