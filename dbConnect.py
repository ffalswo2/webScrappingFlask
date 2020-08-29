import pymysql
from scrapper import *
from gettingListFromDb import *

def connect():
    conn = pymysql.connect(host='localhost', user='root', password='stephan98', db='study_db', charset='utf8')
    curs = conn.cursor()
    conn.commit()

    partTime = get_jobs() # [{"comp":Minjae,"jobs":student,..."adid":10003333},{"comp":....}]

    for row in partTime:

        # comp = job_list()  # ['세븐일레븐','교촌치킨','GS25',...,'도미노피자']
        # place = place_list()  # ['마포구 아현동','신림동 전체',...,'마포구 공덕동']

        company = row["comp"]
        title = row["jobs"]
        location = row["place"]
        pay = row["money"]
        worktime = row["worktime"]
        recently = row["ago"]
        howpay = row["howpay"]
        adid = row["adid"]

        sql = "insert into Alba(comp,jobs,place,money,worktime,ago,howpay,adid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # 데이터 삽입 쿼리
        curs.execute(sql,(company,title,location,pay,worktime,recently,howpay,adid))

        sql2 = "delete from Alba where adid not in (select adid from ( select max(adid) as adid from Alba group by comp,place)as Alba_t);"
        # 중복 제거 쿼리
        curs.execute(sql2)

    conn.commit()
    conn.close()