import psycopg2

try:
           ## REPLACE WITH YOUR CONATAINER IP
   connection = psycopg2.connect(user="postgres",host="192.168.99.100",port="5432",database="postgres")
   cursor = connection.cursor()
   postgres_insert_query = """ INSERT INTO details ( user_id, username, Emp_ID , role) VALUES (%s,%s,%s,%s)"""
## Sample data
   record_to_insert = ( 01,'Manoj','ABC12','Developer')
   cursor.execute(postgres_insert_query, record_to_insert)
   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
	if(connection):
		print("Failed to insert record into mobile table", error)

finally:
	#closing database connection.
	if(connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is closed")
