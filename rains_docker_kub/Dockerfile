FROM eengies/api-rains-predict:0.0.1

ADD com.sh /home/rains_docker/
ADD api/source.py /home/rains_docker/api/
ADD modeles/* /home/rains_docker/modeles/

#####

EXPOSE 8000

CMD uvicorn api.source:app --host 0.0.0.0 --port 8000 --reload

