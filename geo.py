import sqlite3
import json
import codecs

conn = sqlite3.connect('db_big.sqlite')
cur = conn.cursor()

while True :
    print("Please, enter a Year of landslides for the further visualization and press Enter")
    year = input()

    cur.execute('SELECT Disasters.longitude, Disasters.latitude, Places.place_name  FROM Disasters JOIN Places ON Disasters.place_id = Places.id WHERE event_year = ?', (year, ) )

    try:
        cur.fetchone()[0]
        break
    except:
        print('No data for that Year')
        pass



fhand = codecs.open('map.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    lng = row[0]
    lat = row[1]
    where = row[2]
    #cleaning location name from " ' " symbol
    if where.find('\''):
        where = where.replace('\'', '\\\'')

    if lat == 0 or lng == 0 : continue
    try :
        # print(lat, lng, where)
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
fhand.write("year = ["+year+"\n];\n")

cur.close()
fhand.close()

print('---------------------------------------------------------------------------------------')
print(year, "year is chosen")
print(count, "record(s) is(are) found for the chosen year and written to map.js")
print("Open map.html to view the data in a browser")
