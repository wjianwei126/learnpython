
echo "CREATE DATABASE redmine CHARACTER SET utf8;" >./tmp/redmine_db.sql
mysql  < ./tmp/redmine_db.sql

echo "GRANT ALL PRIVILEGES ON redmine.* TO 'redmine'@'localhost' IDENTIFIED BY 'EDCnO0Qgsc' WITH GRANT OPTION;" >./tmp/redmine_user.sql
echo "FLUSH PRIVILEGES;" >>./tmp/redmien_user.sql
mysql  < ./tmp/redmine_user.sql

mkdir -p ./packages/
#rm -f ./packages/*
#wget -qc -P ./packages/ http://www.redmine.org/releases/redmine-2.5.2.tar.gz
wget -qc -P ./packages/ http://www.redmine.org/releases/redmine-2.6.0.tar.gz


tar zxf ./packages/redmine-2.6.0.tar.gz
mkdir -p /home/data/site/old
mkdir -p /home/data/site/redmine
rm -rf /home/data/site/old/*
mv /home/data/site/redmine /home/data/site/old/
mv ./redmine-2.6.0 /home/data/site/redmine
\cp ./conf/database.yml.redmine /home/data/site/redmine/config/database.yml
\cp ./conf/configuration.yml.redmine /home/data/site/redmine/config/configuration.yml
\cp ./conf/additional_environment.rb.redmine /home/data/site/redmine/config/additional_environment.rb

apt-get -y install imagemagick libmagickcore-dev libmagickwand-dev
gem install rmagick

apt-get -y install libmysqlclient-dev

cd /home/data/site/redmine
bundle install --without development test

rake generate_secret_token
RAILS_ENV=production rake db:migrate

useradd redmine
mkdir -p tmp tmp/pdf public/plugin_assets
chown -R redmine:redmine files log tmp public/plugin_assets
chmod -R 755 files log tmp public/plugin_assets

apt-get -y install git
mkdir -p /home/data/files/redmine
chown redmine.redmine /home/data/files/redmine
touch /var/log/redmine.log
chown redmine.redmine /var/log/redmine.log
