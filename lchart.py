import sqlite3

conn = sqlite3.connect('db_big.sqlite')
cur = conn.cursor()

# SELECTING YEAR, FATALITY and COUNTRY from our SQL DB
cur.execute( '''
SELECT Disasters.event_year, Disasters.fatality_count, Country.country_name
FROM Disasters JOIN Places
ON Disasters.place_id = Places.id JOIN Country ON Places.country_id = Country.id WHERE Disasters.fatality_count != 0 ''' )

countries = dict()
for row in cur :
    countries[row[2]] = countries.get(row[2], 0) + row[1]

# pick the top Countries per fatality
top_c = sorted(countries, key=countries.get, reverse=True)
top_c = top_c[:10]
print("Top 10 countries per fatal cases")
print(top_c)

cur.execute( '''
SELECT Disasters.event_year, Disasters.fatality_count, Country.country_name
FROM Disasters JOIN Places
ON Disasters.place_id = Places.id JOIN Country ON Places.country_id = Country.id WHERE Disasters.fatality_count != 0 ''' )

count = 0
fatality = dict()
for row in cur :
    fatality[count] = (row[0],row[1],row[2])
    count +=1

counts = dict()
years = list()

for (id, tuple) in list(fatality.items()):
    country = tuple[2]
    if country not in top_c : continue
    year = tuple[0]
    if year not in years : years.append(year)
    key = (year, country)
    counts[key] = counts.get(key,0) + tuple[1]

years.sort()

fhand = open('lchart.js','w')
fhand.write("lchart = [ ['Year'")
for country in top_c:
    fhand.write(",'"+country+"'")
fhand.write("]")

for year in years:
    fhand.write(",\n['"+str(year)+"'")
    for country in top_c:
        key = (year, country)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")
fhand.close()

print("Output written to lchart.js")
print("Open lchart.htm to visualize the data")
