# Le répertoire 'rains_docker' permet une mise en oeuvre simple des modèle au travers d'une api

# génération et run du conteneur api:
docker-compose up -d --build

#verification
docker container ls
# 3ea45ee9db6a   api-rains-predict   "/bin/sh -c 'uvicorn…


# run test api sur 'localhost:8002'
# test et prediction
./com.sh
# Ok / OK / {"prediction":0} # prediction: pas de pluie

# test via fastapi
http://localhost:8002/docs#/
