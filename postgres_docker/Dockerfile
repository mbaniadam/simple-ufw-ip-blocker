FROM postgres:latest
COPY init.sql /docker-entrypoint-initdb.d/
RUN init.sql
RUN apt-get update && apt install python3 python3-pip libpq-dev 
RUN pip3 install psycopg2
