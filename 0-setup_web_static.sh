#!/bin/bash
#this script set up my web server for deplyment
sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
markup='
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
'
echo "$markup" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "20i\ \tserver_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current;\n\t\tautoindex off;\n\t}" /etc/nginx/nginx.conf
service nginx start
