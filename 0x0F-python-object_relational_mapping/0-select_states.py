#!/usr/bin/python3
import MySQLdb
import sys

# Connect to MySQL database
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows in a list of lists.
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Disconnect from server
db.close()
