#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""


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
    cur.execute("""SELECT * FROM states WHERE name = '{}' ORDER
                BY id ASC""".format(sys.argv[4]))

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    """Execute the list_states function when the script is run."""
    list_states()
