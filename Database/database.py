#database
#using mariaDB
#require pymysql package
#written by Jianqing Ye
import pymysql
from DB import create_table,add_data,look_up
hostIP ='192.168.1.231'
create_table.create_table(hostIP)

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'training_variants.txt'

add_data.add_data(fname,hostIP)
lookup = look_up.look_up
lookup.lookup_id(1,hostIP)

lookup.lookup_Gene('CBL',hostIP)

lookup.lookup_Variation('V430M',hostIP)

lookup.lookup_Class(4,hostIP)
