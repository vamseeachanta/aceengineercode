import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = ("""CREATE TABLE details ( User_ID serial PRIMARY KEY,Username VARCHAR (50) UNIQUE NOT NULL,Emp_ID VARCHAR (50) NOT NULL,
Role VARCHAR (355) UNIQUE NOT NULL)""")
    connection = None
    try:
        ## REPLACE WITH YOUR CONATAINER IP
        connection = psycopg2.connect(user="postgres",host="192.168.99.100",port="5432",database="postgres")
        cursor = connection.cursor()	
		
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

 
if __name__ == '__main__':
    create_tables()		
		
