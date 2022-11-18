#!/usr/bin/python3
'''
Script that list all states from database
'''
from sys import argv
import MySQLdb

def states():
    '''
    This function lists all states from the database hbtn_0e_0_usa
    sorted in ascending order
    '''
    data_base = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3])

    cur = data_base.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY states.id ASC')

    rows = cur.fetchall()
    for row in rows:
        print(row)

    data_base.close

if __name__ == "__main__":
    states()