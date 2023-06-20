import requests
from bs4 import BeautifulSoup
import lxml
import json


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

totalList=[]

for i in range(8):
    url = 'https://comic.naver.com/api/article/list?titleId=739411&page='+str(i)
    res = ((requests.get(url, headers=headers)).json())['articleList']
    result = map(lambda x: [x['subtitle'],'https://comic.naver.com/webtoon/detail?titleId=739411&no={}'.format(x['no'])], res)
    
    A=list(result)
    totalList.extend(A)

totalList = [item for sublist in totalList for item in sublist]
reverseList=totalList[::-1]

linkBox=reverseList[::2]
titleBox=reverseList[1::2]

for k in range(len(titleBox)):
    print(f'왕세자 입학도 [{titleBox[k]}]')
    print(f'바로가기 >>> {linkBox[k]}')
    print(" ")


