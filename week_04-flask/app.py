from flask import Flask, render_template,  jsonify, request  # render_template함수 # 파이썬 jinja(템플릿 변환함수)
app = Flask(__name__)  # Flask클래스의 객체 


@app.route('/', methods=['GET'])  # 페이지 위치 표현 가능 여기서는 홈페이지의 /mypage 경로로 설정하는 경우임, '/' path를 지정   
def home():
   return render_template('index.html')


@app.route('/mypage')   # app.route라는 데코레이터 
def mypage():
    return 'This is My page!'

@app.route('/test', methods=['GET'])
def test_get():
    title = request.args.get('title_give')  # args['title_give']
    return jsonify({'result':'success', 'msg':'GET입니다'})

@app.route('/test', methods=['POST'])
def test_post():
    title = request.form['title_give']
    return jsonify({'result':'success', 'msg':'POST입니다'})


if __name__ == '__main__':  # 앱이 시작되는 지점인 entry point 
   app.run('0.0.0.0',port=5000,debug=True)  # 생성한 app을 실행  // 인자는 주소, 포트, 디버그 입력 가능  1.1.1.1 으로 입력시는 한정된 주소 1.1.1.1만 가능 