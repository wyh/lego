#Introduction

This project is to apply or renew certificates for aliyun cdn automatically. 

User can start the project while docker-compose or kubernetes cronjob.

这个项目的目的是自动从Let's encyrpt 申请证书，并将证书上传至阿里云的CDN

可以在K8S上每个月执行一次

# Steps

1. cp cdn.env.sample cdn.env
2. make changes according to your cdn domain and certificate domain. use a wildcard domain for certificate
3. sudo docker-compose up --build


# for K8S User

1. Please change image repository address
2. change image pull secrets


```
kubectl apply -f ./cronjob.yml
```
