FROM postgres:12-alpine

# RUN apt-get update

USER postgres

RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker

#RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

EXPOSE 5432

VOLUME ["C:\Users\achantv\Documents\volumes\sql\postgres", "/var/log/postgresql", "/var/lib/postgresql"]


# C:\Users\achantv\Documents\volumes\sql\postgres

# WORKDIR /opt/app/mole-analytics

# To run on work computer
# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v C:\Users\achantv\Documents\volumes\sql\postgres:/var/lib/postgresql/data postgres:12-alpine
# For house server
# docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v M:\data\db\postgresql:/var/lib/postgresql/data postgres:12-alpine
