import pymysql

conn = pymysql.connect(host='localhost', user='root', password='stephan98', db='study_db', charset='utf8')
curs = conn.cursor()
conn.commit()

def place_list():
    place_sql = "SELECT place FROM test"
    curs.execute(place_sql)
    place_list = list(curs.fetchall())

    result = []
    for i in place_list:
        string = list(i)[0]
        result.append(string)

    return result

def job_list():
    comp_sql = "SELECT comp FROM test"
    curs.execute(comp_sql)
    comp_list = curs.fetchall()

    result = []
    for i in comp_list:
        string = list(i)[0]
        result.append(string)

    return result