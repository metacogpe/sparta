import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 순위/곡 제목/ 가수를 스크래핑 
# select를 이용해서, tr들을 불러오기 // 
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for music in musics:
    # movie 안에 a 가 있으면,
    rank = music.select_one('td.number')  
    #rank = rank.get_text(" ", strip=True) 
    rank.span.decompose()
    title = music.select_one('td.info > a.title')
    singer = music.select_one('td.info > a.artist')
    print (rank.text.strip(), title.text.strip(), singer.text.strip())
