# import csv, sqlite3

# """
# This file will be left here as legacy, but it is a way to create a sqlite database from
# a csv containedf in a separate folder. (you can look at the link")
# note: 9/25/2022- ERROR. DB NOT UPDATING. FIX LATER.

# """

# con = sqlite3.connect("/home/pi/Documents/Django_files/djenv/test_site/db.sqlite3")#db.sqlite3") # change to 'sqlite:///your_filename.db'
# cur = con.cursor()

# listOfTables = cur.execute(
#   """SELECT name FROM sqlite_master WHERE type='table' AND name='student_performance'; """).fetchall()
# print(listOfTables)
# if listOfTables == []:
#     query = r'"gender","race_ethnicity",' + \
#             r'"parental level of education","lunch","test preparation course",' + \
#             r'"math score","reading score","writing score"'
#     full_query = 'CREATE TABLE student_performance ({0});'.format(query)
#     cur.execute(full_query) # use your column names here

# link = r'/home/pi/Documents/Django_files/djenv/test_site/StudentsPerformance.csv'
# with open(link,'r') as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     dict_from_csv = dict(list(dr)[0])
#     list_of_column_names = list(dict_from_csv.keys())

#     to_db = [
#                 (
#                     i["gender"], i[r"race/ethnicity"],
#                     i["parental level of education"],
#                     i["lunch"], i["test preparation course"],
#                     i["math score"], i["reading score"], i["writing score"]
#                 ) for i in dr
#             ]
# print(len(to_db))
# cur.executemany(r'INSERT INTO student_performance [("gender","race_ethnicity",' + \
#             r'"parental level of education","lunch","test preparation course",' + \
#             r'"math score","reading score","writing score"' + \
#             r')] VALUES (?, ?, ?, ?, ?, ?, ?, ?);', to_db)
# con.commit()
# con.close()

"""
None of the above adds to the db for somne reason. Leaving as legacy. However to add
the csv data to the table simply run
python3 manage.py db shell
.tables
.mode
.import csv_file_location_and_name.csv table_name
and we are done!
"""
