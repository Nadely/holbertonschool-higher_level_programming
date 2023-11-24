#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
import sys


def list_states():
    """Lists all states from the database hbtn_0e_0_usa"""

    # Connect to the database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute the query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
