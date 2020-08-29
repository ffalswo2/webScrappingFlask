#-*- coding: utf-8 -*-

def make_dictionary(job):
    dict = {'comp':job[0],'title':job[1],'location':job[2],'pay':job[3],'worktime':job[4],'recently':job[5],'howpay':job[6]}

    return dict

def make_list(tuplelist):
    job_list = []
    for result in tuplelist:
        dic = make_dictionary(result)
        job_list.append(dic)

    return job_list