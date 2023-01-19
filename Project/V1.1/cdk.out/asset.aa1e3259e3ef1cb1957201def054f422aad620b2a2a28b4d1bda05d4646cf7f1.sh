#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo service httpd start
sudo service httpd enable
echo "<html><h1 style = 'color: rgb(129, 76, 33); text-align: center; font-size: 90px; font-family:Georgia;
margin-top: 100px; background-color: rgb(3, 14, 27); padding: 100px;'>That's one small step for a man, 
one giant leap for the same man</h1></html>" > /var/www/html/index.html
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt
openssl rsa -in privateKey.key -check
openssl x509 -in certificate.crt -text -noout
openssl rsa -in privateKey.key -text > private.pem
openssl x509 -inform PEM -in certificate.crt > public.pem