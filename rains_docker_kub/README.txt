#  Le répertoire 'rains-docker_kub' permet la mise en oeuvre de la prédiction par le biais d'un deployment en cluster 'Kubernetes'.

# start minikube
minikube start

# build the final api image
docker-compose up -d --build
# docker image ls
# api-rains-predict-kub         latest   

# load the image into minikube pool
minikube image load api-rains-predict-kub
# be patient !!

# minikube image ls
# docker.io/library/api-rains-predict-kub:latest

# minikube dashboard --url=true&
# kubectl proxy --address='0.0.0.0' --disable-filter=true&

# deployment
kubectl create -f api-deploy.yml
minikube kubectl -- get pods -A
# default         api-rains-predict-84b54c4884-ffw7x          1/1     Running     0             10s
# default         api-rains-predict-84b54c4884-kx22x          1/1     Running     0             10s

# if failed
# kubectl delete deployment api-rains-predict

# service
kubectl create -f api-service.yml

# ingress
minikube addons enable ingress
kubectl create -f api-ingress.yml

# get the ip@ service access
kubectl get ingress
# ingress-api-rains-predict   nginx   *       192.168.49.2   80      58s
# ADDRESS may not appear imediatly !

# test
./com.sh 192.168.49.2
# OK / OK / {"prediction":0}

# fastapi
# http://192.168.49.2/docs

