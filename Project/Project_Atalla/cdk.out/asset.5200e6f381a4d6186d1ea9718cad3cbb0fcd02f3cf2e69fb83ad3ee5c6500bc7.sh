#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>That's one small step for a man, one giant leap for the same man</h1></html>' > /var/www/html/index.html