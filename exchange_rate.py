# 전세계의 실시간 환율을 텍스트파일로 저장해주는 프로그램
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = requests.get(url)

if res.status_code == 200: # 정상 연결상태면
    txt = res.text
    soup = BeautifulSoup(txt, 'html.parser')
    td_titles = soup.find_all('td', attrs={"class":"tit"})
    td_sales = soup.find_all('td', attrs={"class":"sale"})
    f = open("exchange_rate.txt", 'w', encoding="utf-8")
    f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))+ ' 환율\n\n')
    for i in range(len(td_titles)):
        title = td_titles[i]
        sale = td_sales[i]
        
        f.write(f'{title.a.text.strip()}      {sale.text}\n')

else:
    print(res.status_code)

f.close()
    
    