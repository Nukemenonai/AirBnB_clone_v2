#!/bin/bash
# this script set up my web server for deplyment
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Holberton School" >> /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i "20i\ \tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current;\n\t\tautoindex off;\n\t}" /etc/nginx/nginx.conf
sudo service nginx start
