Le projet 'rains-predict' vise a permettre des predictions meteo  pour un pool de ville d'Australie

Pour ce faire:

1) Apprentissage/Modélisation ('rains_model'):

   A partir d'une base de données au format csv, une phase d'apprentissage automatique est effectué afin de définir des modèles de prédiction:
    . Chaque ville a son propre modèle
    . Les predictions "pour le lendemain" (RainTommorow) ne se font que pour les "journéés courantes sans pluie" (RainToday)

  
2) Mise en oeuvre:
   La mise en oeuvre se fait au travers de conteneurs 'Docker' qui presentent des api de commandes.

   a) Le répertoire 'build-docker' permet la construction des containeurs de base.  Ceux ci seront mise à disposition sur le site 'hub.docker.com'
    compte 'eengies'

   b) Le répertoire 'rains_docker' permet une mise en oeuvre simple des modèle

   c) Le répertoire 'rains_docker_db' complète 'rains_docker' par une base de données permettant de charger la base csv de base ainsi
      que de l'enrichir par de nouveaux enregistrements

   d) Le répertoire 'rains-docker_kub' permet la mise en oeuvre de la prédiction par le biais d'un deployment en cluster 'Kubernetes'.


Chacun des répertoires présente un fichier 'README' décrivant les étapes de construction et de tests/mise en oeuvre

projet disponible sur:
https://github.com/emericericrainsds/rains-predict

# si nécessaire, supprimer les images courantes Docker

docker-compose down
docker stop  `docker container ls -aq`
docker rm  `docker container ls -aq`
docker system prune -a --volumes
docker image ls   
 # ... empty