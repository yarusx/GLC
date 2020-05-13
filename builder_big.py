import sqlite3
import json
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import time

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('db_big.sqlite')
cur = conn.cursor()

url = "https://data.nasa.gov/api/views/dd9e-wu2v/rows.json"

cur.executescript('''
DROP TABLE IF EXISTS Disasters;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Places;

CREATE TABLE Disasters (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    event_date TEXT,
    event_year INTEGER,
    fatality_count INTEGER,
    injury_count INTEGER,
    longitude REAL,
    latitude REAL,
    place_id INTEGER

);

CREATE TABLE Country (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    country_name TEXT UNIQUE

);

CREATE TABLE Places (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    place_name TEXT UNIQUE,
    country_id INTEGER

);

''')

text = "None"

try:
    document = urllib.request.urlopen(url, None, context=ctx)
    text = document.read().decode()
except:
    pass

js = json.loads(text)

count = 0

for item in js["data"]:
    if item[28] == None: continue
    fdate = item[11]
    date = fdate[:10]
    year = fdate[:4]
    if item[13] == None : place = 'No Place Name'
    else: place = item[13]
    if item[21] == None : fatality = 0
    else : fatality = item[21]
    if item[22] == None : injury = 0
    else : injury = item[22]
    country = item[28]
    lng = item[37]
    lat = item[38]


    cur.execute('''INSERT OR IGNORE INTO Country (country_name)
        VALUES ( ? )''', ( country, ) )
    cur.execute('SELECT id FROM Country WHERE country_name = ? ', (country, ))
    country_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Places (place_name, country_id)
        VALUES ( ?, ? )''', ( place, country_id) )
    cur.execute('SELECT id FROM Places WHERE place_name = ? ', (place, ))
    place_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Disasters
        (event_date, event_year, fatality_count,
         injury_count, longitude, latitude, place_id)
        VALUES ( ?, ?, ?, ?, ?, ?, ?  )''',
        ( date, year, fatality, injury, lng, lat, place_id ) )

    # Pause every 100th while commit and pause every 200th for a sec
    count += 1
    if count % 100 == 0 :
        print('Commiting')
        conn.commit()
    if count % 200 == 0 :
        print('Sleep for a 1 sec')
        time.sleep(1)

conn.commit()
cur.close()
