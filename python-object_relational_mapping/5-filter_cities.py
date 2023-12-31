#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""


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
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %(arg)s ORDER BY cities.id",
                {'arg': sys.argv[4]})

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print the results
    cities = [row[0] for row in query_rows]
    print(", ".join(cities))

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    """Execute the list_states function when the script is run."""
    list_states()
