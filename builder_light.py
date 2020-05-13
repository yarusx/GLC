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

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

url = "https://data.nasa.gov/resource/dd9e-wu2v.json"

cur.executescript('''
DROP TABLE IF EXISTS Disasters;
DROP TABLE IF EXISTS Landslide_Cat;
DROP TABLE IF EXISTS Landslide_Tr;
DROP TABLE IF EXISTS Landslide_Sz;
DROP TABLE IF EXISTS Country;

CREATE TABLE Disasters (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    event_date TEXT,
    location_description TEXT,
    fatality_count INTEGER,
    injury_count INTEGER,
    longitude REAL,
    latitude REAL,
    lan_cat_id INTEGER,
    lan_siz_id INTEGER,
    lan_tr_id INTEGER,
    countr_id INTEGER

);

CREATE TABLE Landslide_Cat (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    landslide_category TEXT UNIQUE

);

CREATE TABLE Landslide_Tr (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    landslide_trigger TEXT UNIQUE

);

CREATE TABLE Landslide_Sz (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    landslide_size TEXT UNIQUE

);

CREATE TABLE Country (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    country_name TEXT UNIQUE

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

for row in js:
    fdate = row["event_date"]
    date = fdate[:10]
    try: location = row["location_description"]
    except: location = "NoData"
    lcat = row["landslide_category"]
    try: ltrig = row["landslide_trigger"]
    except: ltrig = "unknown"
    try: lsize = row["landslide_size"]
    except: lsize = "unknown"
    try: fatality = row["fatality_count"]
    except: fatality = 0
    try: injury = row["injury_count"]
    except: injury = 0
    try: country = row["country_name"]
    except: country = "NoData"
    lng = row["longitude"]
    lat = row["latitude"]

    cur.execute('''INSERT OR IGNORE INTO Country (country_name)
        VALUES ( ? )''', ( country, ) )
    cur.execute('SELECT id FROM Country WHERE country_name = ? ', (country, ))
    countr_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Landslide_Cat (landslide_category)
        VALUES ( ? )''', ( lcat, ) )
    cur.execute('SELECT id FROM Landslide_Cat WHERE landslide_category = ? ', (lcat, ))
    lan_cat_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Landslide_Tr (landslide_trigger)
        VALUES ( ? )''', ( ltrig, ) )
    cur.execute('SELECT id FROM Landslide_Tr WHERE landslide_trigger = ? ', (ltrig, ))
    lan_tr_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Landslide_Sz (landslide_size)
        VALUES ( ? )''', ( lsize, ) )
    cur.execute('SELECT id FROM Landslide_Sz WHERE landslide_size = ? ', (lsize, ))
    lan_siz_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Disasters
        (event_date, location_description, fatality_count,
         injury_count, longitude, latitude, lan_cat_id, lan_siz_id, lan_tr_id, countr_id)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?  )''',
        ( date, location, fatality, injury, lng, lat, lan_cat_id, lan_siz_id, lan_tr_id, countr_id ) )

    # Pause every 50th while commit and pause every 100th for a sec
    count += 1
    if count % 100 == 0 :
        print('Commiting')
        conn.commit()
    if count % 200 == 0 :
        print('Sleep for a 1 sec')
        time.sleep(1)

conn.commit()
cur.close()
