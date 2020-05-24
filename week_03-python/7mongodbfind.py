from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 



# 매트릭스 평점 가져오기
target_movie = db.movies.find_one({'title':'매트릭스'})
print(target_movie['star'])


def getStarFromTitle(title):
    star = db.movies.find_one({'title':title})['star']
    return star

def getTitlesFromTitle(title):
    star = getStarFromTitle(title)
    movies = list(db.movies.find({'star':star}))
    titles = []
    for movie in movies:
        titles.append(movie['title'])
    return titles

for title in getTitlesFromTitle('매트릭스'):
    print(title)


