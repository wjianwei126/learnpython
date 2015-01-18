rm -f ./tmp/*
wget -qcP ./tmp/ http://nginx.org/keys/nginx_signing.key
apt-key add ./tmp/nginx_signing.key
echo "deb http://nginx.org/packages/debian/ wheezy nginx" > /etc/apt/sources.list.d/nginx.list
echo "deb-src http://nginx.org/packages/debian/ wheezy nginx" >> /etc/apt/sources.list.d/nginx.list

apt-get update
apt-get -y install nginx

gem install passenger
apt-get install libcurl4-gnutls-dev
passenger-install-nginx-module

\cp ./conf/nginx.rails /etc/init.d/nginx.rails
chmod +x /etc/init.d/nginx.rails
\mv /opt/nginx/conf/nginx.conf /opt/nginx/conf/nginx.conf.old
\cp ./conf/nginx.conf.redmine /opt/nginx/conf/nginx.conf
