docker-compose down
docker stop  `docker container ls -aq`
docker rm  `docker container ls -aq`
docker system prune -a --volumes
docker image ls 