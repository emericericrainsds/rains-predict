# Le répertoire 'build-docker' permet la construction des containeurs de base (pour l'api et pour la base de données sql).

# Ceux ci sont mise à disposition sur:
# https://hub.docker.com/repositories/eengies

# Il n'est donc pas nécessaire de faire les oérations qui suivent... 

# génération des images
docker-compose up -d --build


# push des images sur hub.docker.com ( account eengies)

docker tag api-rains-predict eengies/api-rains-predict:0.0.1
docker tag db-rains-predict eengies/db-rains-predict:0.0.1
docker push eengies/db-rains-predict:0.0.1
docker push eengies/api-rains-predict:0.0.1

# verify on your account 
# https://hub.docker.com/repositories
