#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo service httpd start
sudo service httpd enable
echo "<html><h1>That's one small step for a man, one giant leap for the same man</h1></html>" > /var/www/html/index.html