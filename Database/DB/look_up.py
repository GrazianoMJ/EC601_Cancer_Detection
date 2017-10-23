#function to lookup data in mariaDB
#written by Jianqing Ye
#yjq@bu.edu
#OCT 22 2017
import pymysql
class look_up():

    def lookup_id(cancer_id):
        conn = pymysql.connect(host ='localhost',user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
        cur = conn.cursor()

        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancer_detection.cancer WHERE cancer_id = %s'''
        cur.execute(sql,(cancer_id,))
        result = cur.fetchall()
        print('cancer_id =',cancer_id,'\n','result = \n',result)
        conn.close()

    def lookup_Gene(Gene):
        conn = pymysql.connect(host ='localhost',user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
        cur = conn.cursor()

        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancer_detection.cancer WHERE Gene = %s'''
        cur.execute(sql,(Gene,))
        result = cur.fetchall()
        print('Gene =',Gene,'\n','result = \n',result)
        conn.close()

    def lookup_Variation(Variation):
        conn = pymysql.connect(host ='localhost',user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
        cur = conn.cursor()

        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancer_detection.cancer WHERE Variation = %s'''
        cur.execute(sql,(Variation,))
        result = cur.fetchall()
        print('Variation =',Variation,'\n','result = \n',result)
        conn.close()

    def lookup_Class(Class):
        conn = pymysql.connect(host ='localhost',user ='root',password ='EC601',database ='cancer_detection',charset ='utf8mb4')
        cur = conn.cursor()

        sql = '''SELECT cancer_id,Gene,Variation,Class FROM cancer_detection.cancer WHERE Class = %s'''
        cur.execute(sql,(Class,))
        result = cur.fetchall()
        print('class =',Class,'\n','result = \n',result)
        conn.close()
