#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
TESTPATH=/data/web_static/releases/test
echo "Holberton School" | sudo tee "${TESTPATH}"/index.html > dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data

FILENAME=/etc/nginx/sites-available/default
line=1
while read strline; do
	if [[ $strline == *"location"* ]]
	then
		break
	fi
	((line+=1))
done < $FILENAME
l1="\n\tlocation /hbnb_static/ {\n"
l2="\t\talias /data/web_static/current/;\n"
l3="\t}\n"
newloc="${l1}${l2}${l3}"
sudo sed -i "${line}i\\${newloc}" $FILENAME

sudo service nginx restart
exit 0
