#database
#using mariaDB
#require pymysql package
#written by Jianqing Ye
import pymysql
from DB import create_table,add_data,look_up
endpoint = 'cancerdetection.citobxwciwnc.us-east-1.rds.amazonaws.com'
#create_table.create_table(endpoint)

#fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'training_variants.txt'

#add_data.add_data(fname,endpoint)
lookup = look_up.look_up
lookup.lookup_id(1,endpoint)

lookup.lookup_Gene('CBL',endpoint)

lookup.lookup_Variation('V430M',endpoint)

lookup.lookup_Class(4,endpoint)
