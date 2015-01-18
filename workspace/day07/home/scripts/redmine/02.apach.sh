apt-get update
apt-get -y install apache2 libapache2-mod-passenger bundler rails

\cp ./conf/redmine_apache_conf /etc/apache2/sites-available/redmine
a2ensite redmine
service apache2 restart
