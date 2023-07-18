import psycopg2
import datetime
import subprocess
import os

today = datetime.date.today()
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

def main():
    #cursor.execute(f"SELECT * FROM {table_name}")
    #selected = cursor.fetchall()
    cursor.execute(f"select username, ip_address, expire_date, created_date, valid_days from users ")
    selected = cursor.fetchall()
    for i in selected:
        userIP = i[1]
        userAge = i[2] - today
        checkUfwUsers =subprocess.call(f"ufw status | grep -w {userIP}",shell=True)
        print(userIP, userAge.days)
        if userAge.days <= 0:
            print("user expired!")
            if checkUfwUsers != 0:
                os.system(f"ufw deny from {userIP}")
        elif userAge.days > 0:
            if checkUfwUsers == 0:
                os.system(f"ufw delete deny from {userIP}")

main()