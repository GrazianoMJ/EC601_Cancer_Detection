#function to lookup data in mariaDB
#written by Jianqing Ye
#yjq@bu.edu
#OCT 22 2017
import pymysql
class look_up():

    def lookup_id(cancer_id,hostIP):
        conn = pymysql.connect(host =hostIP,user ='root',password ='cancerdetection',database ='cancerdetection',charset ='utf8mb4')
        cur = conn.cursor()
        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancerdetection.cancer WHERE cancer_id = %s'''
        cur.execute(sql,(cancer_id,))
        result = cur.fetchall()
        print('cancer_id =',cancer_id,'\n','result = \n',result)
        conn.close()

    def lookup_Gene(Gene,hostIP):
        conn = pymysql.connect(host =hostIP,user ='root',password ='cancerdetection',database ='cancerdetection',charset ='utf8mb4')
        cur = conn.cursor()
        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancerdetection.cancer WHERE Gene = %s'''
        cur.execute(sql,(Gene,))
        result = cur.fetchall()
        print('Gene =',Gene,'\n','result =')
        for item in result:
            print(item)
        conn.close()

    def lookup_Variation(Variation,hostIP):
        conn = pymysql.connect(host =hostIP,user ='root',password = 'cancerdetection',database ='cancerdetection',charset ='utf8mb4')
        cur = conn.cursor()
        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancerdetection.cancer WHERE Variation = %s'''
        cur.execute(sql,(Variation,))
        result = cur.fetchall()
        print('Variation =',Variation,'\n','result =')
        for item in result:
            print(item)
        conn.close()

    def lookup_Class(Class,hostIP):
        conn = pymysql.connect(host =hostIP,user ='root',password ='cancerdetection',database ='cancerdetection',charset ='utf8mb4')
        cur = conn.cursor()
        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancerdetection.cancer WHERE Class = %s'''
        cur.execute(sql,(Class,))
        result = cur.fetchall()
        print('class =',Class,'\n','result =')
        for item in result:
            print(item)
        conn.close()
