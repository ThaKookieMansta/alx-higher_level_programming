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
    (db_cursor.execute
     ("SELECT cities.id, cities.name, states.name FROM `cities` "
      "INNER JOIN `states` ON cities.state_id=states.id ORDER BY "
      "cities.id"))
    [print(city) for city in db_cursor.fetchall()]
