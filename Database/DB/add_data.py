#function to add data in mariaDB
#written by Jianqing Ye
#yjq@bu.edu
#OCT 22 2017

import pymysql

def add_data(fname):
    conn = pymysql.connect(host ='localhost',user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
    cur = conn.cursor()


    count = 0
    with open(fname) as f:
        next(f)
        for line in f:
            r = line.rstrip().split(',')
            cancer_id = r[0]
            Gene = r[1]
            Variation = r[2]
            Class = r[3]
            print(Gene)
            sql = '''INSERT INTO cancer(cancer_id,Gene,Variation,Class) VALUES(%s,%s,%s,%s)'''
            cur.execute(sql,(cancer_id,Gene,Variation,Class))
            count+= 1
    conn.commit()
    print('%d data insterted!',count)
