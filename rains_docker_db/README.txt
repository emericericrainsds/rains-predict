#  Le répertoire 'rains_docker_db' complète 'rains_docker' par une base de données permettant de charger la base csv de base ainsi
#  que de l'enrichir par de nouveaux enregistrements

# génération et run du conteneur api:
docker-compose up -d --build

# verification
docker container ls
# 11f3cc3ea865   db-rains-predict    "docker-entrypoint.s…
# 3ea45ee9db6a   api-rains-predict   "/bin/sh -c 'uvicorn…


# run test api sur 'localhost:8002'
# test et prediction
./com.sh
# Ok / OK / {"prediction":0} # prediction: pas de pluie

# test via fastapi
http://localhost:8002/docs#/
