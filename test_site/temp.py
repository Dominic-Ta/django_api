import csv, sqlite3

"""
This file will be left here as legacy, but it is a way to create a sqlite database from
a csv containedf in a separate folder. (you can look at the link")

"""

con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
query = r'"gender","race_ethnicity",' + \
        r'"parental level of education","lunch","test preparation course",' + \
        r'"math score","reading score","writing score"'
full_query = 'CREATE TABLE student_performance ({0});'.format(query)

cur.execute(full_query) # use your column names here
link = r'/home/pi/Documents/databases_csv_txt_files/StudentsPerformance.csv'
with open(link,'r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    dict_from_csv = dict(list(dr)[0])
    list_of_column_names = list(dict_from_csv.keys())
    print(list_of_column_names)
    to_db = [
                (
                    i["gender"], i[r'race/ethnicity'],
                    i["parental level of education"],
                    i["lunch"], i["test preparation course"],
                    i["math score"], i["reading score"], i["writing score"]
                ) for i in dr
            ]

cur.executemany(r'INSERT INTO student_performance ("gender","race_ethnicity",' + \
            r'"parental level of education","lunch","test preparation course",' + \
            r'"math score","reading score","writing score"' + \
            r') VALUES (?, ?, ?, ?, ?, ?, ?, ?);', to_db)
con.commit()
con.close()
