FROM postgres:alpine

ENV POSTGRES_PASSWORD secret

COPY init.sql /docker-entrypoint-initdb.d/
