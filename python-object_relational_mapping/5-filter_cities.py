#!/usr/bin/python3
'''
Script that list all cities from database
'''
from sys import argv
import MySQLdb


def cities():
    '''
    This function lists all cities from the database hbtn_0e_4_usa
    '''
    data_base = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    if ';' in argv[4]:
        return

    cur = data_base.cursor()
    query = "SELECT t1.id, t1.name, t2.name FROM cities t1 \
             LEFT JOIN states t2 ON t1.state_id = t2.id \
             ORDER BY t1.id ASC".format(argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for i,  row in enumerate(rows):
        if i > 0:
            print(', ', end="")
        print(row[1], end="")
    print()

    data_base.close


if __name__ == "__main__":
    cities()
