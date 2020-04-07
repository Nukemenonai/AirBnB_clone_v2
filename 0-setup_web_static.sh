#!/bin/bash
#this script set up my web server for deplyment
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" >> /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i "20i\ \tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current;\n\t\tautoindex off;\n\t}" /etc/nginx/nginx.conf
sudo service nginx start
