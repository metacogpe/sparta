from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
db.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})

all_users = list(db.users.find()) #커서를 생성 후 all_users라는 리스트로 저장'''
print(all_users)

condition_users = list(db.users.find({'age':21}))
print(condition_users)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})