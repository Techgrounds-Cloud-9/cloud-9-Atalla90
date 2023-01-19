#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo service httpd start
sudo service httpd enable
sudo yum install -y mod24_ssl
sudo service httpd restart
echo "<html><h1 style = 'color: rgb(129, 76, 33); text-align: center; font-size: 90px; font-family:Georgia;
margin-top: 100px; background-color: rgb(3, 14, 27); padding: 100px;'>That's one small step for a man, 
one giant leap for the same man</h1></html>" > /var/www/html/index.html