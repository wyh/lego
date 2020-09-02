if [ -d "/aliyun/.lego/certificates/" ];
then
   cmd=renew
else
   cmd=run
fi

lego --domains $domain --email $email --dns alidns --accept-tos --dns.disable-cp --dns.resolvers $resolver $cmd

python3 upload.py $ALICLOUD_ACCESS_KEY $ALICLOUD_SECRET_KEY $dns_domains
