import psycopg2

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
finish = 0

while finish == 0:
    finish = 1
    print("                         Add wg peers")
    user = input("Enter User: ")
    ip_address = input("Enter ip_address: ")
    expire_date = input("Format: yyyy/mm/dd\nEnter expiration date: ")
    """ insert a new user into the users table """
    sql = f"""INSERT INTO {table_name} (username,ip_address,expire_date) VALUES ('{user}','{ip_address}','{expire_date}')"""
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







