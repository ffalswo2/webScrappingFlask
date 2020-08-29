import csv

def save_to_file(jobs): # csv 파일로 저장
    file = open("alba.csv",mode="w")
    writer = csv.writer(file)
    writer.writerow(["company","Title","Location","Pay","Worktime","Recently","Howpay"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return