import requests
from bs4 import BeautifulSoup
import lxml

url="https://media.naver.com/press/028/ranking?type=popular"
res=requests.get(url)
webpage=res.text

soup=BeautifulSoup(webpage,"lxml")

a_title_tag=soup.find_all(name="strong",class_="list_title")
a_title_link=soup.find_all(name="a",class_="_es_pc_link")
a_title_textBox=[]
a_title_linkBox=[]

for title in a_title_tag:
    a_title_textBox.append(title.get_text())

for link in a_title_link:
    a_title_linkBox.append(link.get("href"))

# print(a_title_textBox)
# print("\n")
# print(a_title_linkBox)

print("<<< 한겨례신문 랭킹 1위~20위 기사 목록 >>>")
print("\n")

rank=1
for i in range(len(a_title_textBox)):
    print(str(rank)+".",a_title_textBox[i],">>>바로가기>>>",end=" ")
    print(a_title_linkBox[i])
    rank+=1
    print()

