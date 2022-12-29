docker-compose up -d --build

minikube start

minikube image load api-rains-predict


#minikube dashboard --url=true&
#kubectl proxy --address='0.0.0.0' --disable-filter=true&

kubectl create -f api-deploy.yml
minikube kubectl -- get pods -A

kubectl create -f api-service.yml
kubectl create -f api-ingress.yml

#kubectl delete deployment api-rains-predict

kubectl get ingress

curl -X GET -i http://192.168.49.2:80/RainsPredict/2012-01-13:Perth:23.8:34.9:0:13.2:12.4:NE:39:ENE:ENE:19:15:51:37:1013:1009.4:0:4:27.6:33.1:No
