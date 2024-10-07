import requests
from bs4 import BeautifulSoup
import pandas as pd 

# 웹에 접속
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/chart/index.htm",headers=header)
print(r) #접속이 잘됐는지 확인

soup = BeautifulSoup(r.text, 'html.parser') #html 정보 가지고오기
# print(soup) #가져온 html 데이터 출력

rank = []  #리스트 변수
# 1-100까지 리스트 만들기
for i in range(1, 101):
    rank.append(i)
print(rank)

# #conts > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a


tlist = []
#제목
title = soup.select('div.ellipsis.rank01 > span > a')
#for t in title:
#    print(t.text)
for t in title:
    tlist.append(t.text)   #노래제목 리스트 만들기

#가수 리스트 만들기
alist = []
artist = soup.select('div.ellipsis.rank02 > span > a:nth-child(1)')
for a in artist:
    alist.append(a.text)

df3 = pd.DataFrame({'순위': rank,
                    '제목': tlist,
                    '가수': alist})

df3.to_csv('melon100.csv', index=False)


#for i in range(0,100):
    # if artist[i].text != '임영웅':  #특정 가수 빼고 출력
    # if artist[i].text == '임영웅':  #특정 가수만 출력
 #   print(f'{i+1}위 {title[i].text} - {artist[i].text}')

