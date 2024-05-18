import mysql.connector

data_base=mysql.connector.connect(
	host='localhost',
	user='root',
	password='pupos2022')

# prepare a cursor object
cursor_object=data_base.cursor()

# create database
cursor_object.execute('CREATE DATABASE my_database')

print('All done!')
