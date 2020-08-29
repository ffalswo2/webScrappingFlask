#-*- coding: utf-8 -*-

import pymysql
from flask import Flask, render_template,request,redirect,send_file
from export import save_to_file
from dbConnect import connect
from databaseResult import make_list,make_dictionary

app = Flask("AlbaScrapper")

conn = pymysql.connect(host='localhost', user='root', password='stephan98', db='study_db', charset='utf8')
curs = conn.cursor()
conn.commit()

# connect()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    strarea = request.args.get('area')

    if strarea:
        sql = f"SELECT * FROM Alba where binary(place) like '%{strarea}%';"
        curs.execute(sql)
        result = curs.fetchall()
        if result:
            jobs = result
            job = make_list(jobs)
        else:
            return redirect("/")
    else:
        return redirect("/")
    return render_template("report.html",searchingBy = request.args.get('area'),resultsNumber=len(job),alba=job)

@app.route("/export")
def export():
    strarea = request.args.get('area')
    # print(strarea)

    if strarea:
        sql = f"SELECT * FROM Alba where binary(place) like '%{strarea}%';"
        curs.execute(sql)
        result = curs.fetchall()

        if result:
            jobs = result
            job = make_list(jobs)
            save_to_file(job)
        return send_file("alba.csv")
    else:
        return redirect("/")

    #     if not result:
    #         raise Exception()
    #     save_to_file(result)
    #     return send_file("alba.csv")
    # except:
    #     return redirect("/")

app.run()