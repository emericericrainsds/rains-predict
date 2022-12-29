FROM debian:latest

RUN apt-get update && apt-get install -y python3 python3-pip python3-pandas
RUN pip install "fastapi[all]" uvicorn scikit-learn
#RUN apt-get -y install postgresql postgresql-contrib
RUN apt-get install -y python3-dev libpq-dev
RUN pip install psycopg2

WORKDIR /home/rains_docker/api
WORKDIR /home/rains_docker/modeles
WORKDIR /home/rains_docker/templates
WORKDIR /home/rains_docker/


