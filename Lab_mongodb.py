from pymongo import MongoClient
from random import randint
from pprint import pprint

def test_len(data_list):
    for i in range(len(data_list)-1):
        flag = len(data_list[i])==len(data_list[i+1])
        if not flag:
            raise ValueError("len of {} and {} is not the same".format(i,i+1))            

client = MongoClient('mongodb+srv://theo:pass12345@cluster0-8upze.mongodb.net/test?retryWrites=true&w=majority')
db=client.lab

names = ['Theodore','Godwin','Vania','Duta','Amo','Josafat','Selvy','Shodiq','Ais','Murti','Ika','Wilda']
batch = [2015,2015,2015,2015,2015,2015,2015,2016,2016,2017,2016,2017]
degree = ['s1','s1','s1','s1','s1','s1','s1','s1','s1','s1','s3','s2']
specialty = ['Image Processing','Device Optik','Fiber Optic','Spectroscopy','Fiber Optic','Spectroscopy','Spectroscopy','Device Optik','Device optik','Spectroscopy','Fiber Optic','Spectroscopy']

data_list = [names,batch,degree,specialty]

test_len(data_list)

for i in range(len(names)):
    member = {
        'name' : names[i],
        'batch' : batch[i],
        'degree' : degree[i],
        'specialty' : specialty[i] 
    }

    result=db.member.insert_one(member)

    print('Update Member {0} as {1}'.format(i+1,result.inserted_id))

