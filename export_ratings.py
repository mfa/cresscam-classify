#!/usr/bin/python3

""" export ratings from shotwell database
"""
import csv
import os.path
import sqlite3
import sys


db_file = os.path.join(os.environ.get("HOME"), '.local/share/shotwell', 'data', 'photo.db')
conn = sqlite3.connect(db_file)
c = conn.cursor()
rows = c.execute('SELECT filename, rating FROM phototable WHERE rating > 0 ORDER BY filename;')
csvwriter = csv.writer(sys.stdout, delimiter=';')
csvwriter.writerow(["filename", "rating"])
for (filename, rating) in rows:
    csvwriter.writerow([os.path.basename(filename), rating])
