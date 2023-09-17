#!/usr/bin/python3

"""
This script lists all states from the db hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    selected_db = MySQLdb.connect(user=sys.argv[1],
                                  passwd=sys.argv[2],
                                  db=sys.argv[3])
    db_cursor = selected_db.cursor()
    db_cursor.execute("SELECT * FROM `states`")
    [print(state) for state in db_cursor.fetchall() if state[1] == sys.argv[4]]
