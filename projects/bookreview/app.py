from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # form 데이터를 읽어오기  // 데이터 작성 후 전체를 넘겨 주는 형태를 form이라고 함, body에서 데이터 읽어오기 
    print(request.form)
    title = request.form['title']   # request함수의 form이라는 딕셔너리 정보 활용
    author = request.form['author']
    review = request.form['review']

    review_dict = {
        'title' : title,
        'author' : author,
        'review' : review
    }
    print(review_dict)
    # mongodb에 저장하기 
    db.reviewtable.insert_one(review_dict)  # dictionary 데이터 형태를 그대로 인서트 가능 


    # 성공여부 반환하기 
    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # 1. 모든 reviews의 문서를 가져온 후 list로 변환합니다.
    storedreviews = list(db.reviewtable.find({}))
    reviews = []

    for storedreview in storedreviews:
        reviews.append({
            'title':storedreview['title'],
            'author':storedreview['author'],
            'review':storedreview['review']
        })
        
    print(storedreviews)

	# 2. 성공 메시지와 함께 리뷰를 보냅니다.
    return jsonify({'result':'success', 'reviews': reviews, 'msg':'포스팅 완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)