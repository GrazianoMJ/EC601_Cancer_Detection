#database
#using mariaDB
#require pymysql package
#written by Jianqing Ye

from DB import create_table,add_data,look_up
create_table.create_table()

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'training_variants.txt'

add_data.add_data(fname)

look_up.look_up.lookup_id(1)

look_up.look_up.lookup_Gene('CBL')

look_up.look_up.lookup_Variation('V430M')

look_up.look_up.lookup_Class(2)
