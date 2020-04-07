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
new_str="\tlocation \/hbnb_static\/ {\n\t#alias \/data\/web_static\/current;\n\tautoindex off;\n\t}"
sed -i "20i\ $new_strcase  in" /etc/nginx/nginx.conf
sudo service nginx start
