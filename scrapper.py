#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
# &page={page}

LIMIT = 50

def get_last_page(url): # 마지막 페이지 찾기
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    pagenation = soup.find("div",id="NormalInfo").find("strong").get_text(strip=True)
    last = pagenation.replace(',','')

    last_page = int(last)

    if last_page % LIMIT > 0:
        last_page = (last_page // LIMIT) + 1
    else:
        last_page = last_page // LIMIT

    return last_page

def normalize(s):
    if s == None:
        return 0
    elif s != None:
        return s.replace(',','').strip().replace('원','').strip()

def extract_job(html): # 필요한 값 찾아서 딕셔너리로 반환
    title = html.find("span",{"class":"title"}).get_text(strip=True)
    company = html.find("span",{"class":"company"}).get_text(strip=True)
    location = html.find("td",{"class":"local"}).get_text(strip=True)
    workTime = html.find("td",{"class":"data"}).get_text(strip=True)
    pay = html.find("span",{"class":"number"}).get_text(strip=True)
    wage = int(normalize(pay))
    howPay = html.find("span",{"class":"payIcon"}).get_text(strip=True)
    recently = html.find("td",{"class":"regDate"}).get_text(strip=True)
    adid = html.find("a")['href'][21:]

    dic = {'comp': company, 'jobs': title, 'place': location, 'money': wage, 'worktime': workTime,'ago': recently, 'howpay': howPay, 'adid': adid}
    # if '' in list(dic.values()):
    #     i = list(dic.values()).index('')
    #     keys = list(dic.keys())
    #     dic[keys[i]] = 'None'
    return dic

def extract_jobs(last_page, url): # 딕셔너리값 받아서 리스트에 저장
    jobs = []
    for page in range(last_page):
        print(f"Scraping Heaven page: {page + 1}")
        result = requests.get(f"{url}&page={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("tr" and "tr",{"class":"divide"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs

def get_jobs(): # 실행 함수
    url = f"http://www.alba.co.kr/job/area/MainLocal.asp?schnm=LOCAL&viewtype=L&sidocd=02&gugun=&d_areacd=&hidListView=LIST&hidSortCnt=50&gendercd=C01&strAreaMulti="
    last_page = get_last_page(url)
    alba = extract_jobs(last_page, url)

    return alba

def get_jobs_place(strarea):
    url = f"http://www.alba.co.kr/job/area/MainLocal.asp?schnm=LOCAL&viewtype=L&sidocd=02&gugun=&d_areacd=&hidListView=LIST&hidSortCnt=50&gendercd=C01&strAreaMulti={strarea}"
    last_page = get_last_page(url)
    alba = extract_jobs(last_page, url)

    return alba

