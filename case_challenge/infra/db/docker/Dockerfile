FROM postgres:14-alpine

COPY create-databases.sh /docker-entrypoint-initdb.d/

EXPOSE 5432

RUN chmod +x /docker-entrypoint-initdb.d/create-databases.sh