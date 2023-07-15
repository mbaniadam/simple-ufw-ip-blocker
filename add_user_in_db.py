import psycopg2
from datetime import timedelta, date

db_name = "wgpeers"
table_name = "users"
db_host = "127.0.0.1"
db_port =  5432
cnx = psycopg2.connect(database=db_name,
                        host=db_host,
                        user="postgres",
                        password="pgmor@1010",
                        port=db_port)
cursor = cnx.cursor()

def addUpUser():
    finish = 0
    while finish == 0:
        finish = 1
        print("                         Add wg peers")
        user = input("Enter User: ")
        ip_address = input("Enter ip_address: ")
        validDays = int(input("Valid days: "))
        expire_date = date.today() + timedelta(days=validDays)
        """ insert a new user into the users table """
        sql = f"""INSERT INTO {table_name} (username,ip_address,expire_date,valid_days) VALUES ('{user}','{ip_address}','{expire_date}',{validDays})
                ON CONFLICT (ip_address) DO UPDATE SET expire_date = EXCLUDED.expire_date;"""
        try:
            cursor.execute(sql)
            #print(cursor.execute(f"INSERT IGNORE INTO {table_name} ({user}, {ip_address}, {expire_date}) VALUES (%s,%s,%s)",
            #    (user,ip_address,expire_date)))
            end = input("would you like add another record? (y/n) ")
            if end == "y":
                finish = 0
            else:
                cnx.commit()
                continue
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    cnx.close()


def removeUser():
    finish = 0
    while finish == 0:
        finish = 1
        print("                         Remove wg peers")
        ip_address = input("Enter ip_address: ")
        sql = f"""DELETE FROM {table_name} WHERE ip_address = '{ip_address}';"""
        try:
            cursor.execute(sql)
            end = input("would you like remove another record? (y/n) ")
            if end == "y":
                finish = 0
            else:
                cnx.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    cnx.close()




X = input("Add or Update >>> 1 - Remove >>> 2 : ")
if X == "1":
    addUpUser()
elif X == "2":
    removeUser()
else:
    print("wrong input!")