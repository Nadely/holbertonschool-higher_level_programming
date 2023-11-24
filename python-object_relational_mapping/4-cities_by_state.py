#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
            "JOIN states ON cities.state_id = states.id ORDER BY cities.id")


query_rows = cur.fetchall()
for row in query_rows:
    print(row)

cur.close()
conn.close()
