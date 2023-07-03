import mysql.connector as mysql
import csv
#Connect DB server and database
conn = mysql.connect(user='root', password='Shivamkanha2002@', host='localhost', database='testdatabase')
cursor = conn.cursor()
#open the csv file
with open('HINDALCO_1D.xlsx - HINDALCO.csv', mode='r') as csv_file:
    #read csv using reader class
    csv_reader = csv.reader(csv_file)
    #skip header
    header = next(csv_reader)
    #Read csv row wise and insert into table
    for row in csv_reader:
        sql = "INSERT INTO data(datetime, close, high,low,open,volume,instrument) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        
    print("Record inserted")   
 
conn.commit()
cursor.close()