#function to add table in mariaDB
#written by Jianqing Ye
#yjq@bu.edu
#OCT 22 2017

import pymysql


def create_table(hostIP):
    conn = pymysql.connect(host =hostIP,user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS cancer;
        CREATE TABLE cancer(
        id int primary key auto_increment not null,
        cancer_id int(20) not null,
        Gene varchar(100) not null,
        Variation varchar(100) not null,
        Class int(20)
        )

    ''')
    conn.commit()
