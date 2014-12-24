#!/usr/bin/python

import os
import psycopg2
import sys
import pprint
import gspread
from config import *

#list=os.listdir('/etc')
# #Define our connection string
#conn_string = "host= dbhost dbname= dbname user= dbuser password= dbpw"
# # get a connection, if a connect cannot be made an exception will be raised here
#conn = psycopg2.connect(conn_string)
# # conn.cursor will return a cursor object, you can use this cursor to perform queries
#cursor = conn.cursor()

gc = gspread.login( googleemail, googlepw )

wks = gc.open(workbook).sheet1


######################################################################################

list=os.listdir(location)
wks.update_acell('A1', "id")
wks.update_acell('B1', "film")
i=1
cell=2
#verwijder alle records in de DB
#query1="DELETE FROM films"
#cursor.execute(query1)
for item in list:
	# # voeg folder namet toe aan de datebase
	cell1= "A" + str(cell)
	cell2= "B" + str(cell)
	# query2="INSERT INTO films (id, name) VALUES ("+str(i)+",'"+item+"')"
	# cursor.execute(query2)
	# conn.commit()
	wks.update_acell(cell1, str(i))
	wks.update_acell(cell2, item)
	if os.path.isfile(item): pass
	
	else:print (item)
	i=i+1
	cell=cell+1
	
# conn.close()
