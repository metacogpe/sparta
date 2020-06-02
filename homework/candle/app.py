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

@app.route('/orders', methods=['POST'])
def order():
	# 1. 클라이언트로부터 데이터를 받기
    ordername = request.form['ordername']
    qunatity = request.form['qunatity']
    address = request.form['address']
    phoneno = request.form['phoneno']
	# 2. DB에 삽입할 order 만들기
    order = {
        'ordername':ordername,
        'qunatity':qunatity,
        'address':address,
        'phoneno':phoneno
    }
	# 3. mongoDB에 데이터를 넣기
    db.orders.insert_one(order)    
    return jsonify({'result': 'success', 'msg':'주문신청되었습니다!'})

@app.route('/orders', methods=['GET'])
def read_orders():
    # 1. DB에서 주문 정보 모두 가져오기
    orders = list(db.orders.find({},{'_id':0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result':'success', 'orders': orders})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)