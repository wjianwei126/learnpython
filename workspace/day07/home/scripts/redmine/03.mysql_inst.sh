apt-get -y  update
apt-get -y install mysql-server-5.5

#\cp ./conf/my.cnf_5.5_utf8 /etc/mysql/my.cnf

#mysql_install_db --user=mysql --datadir=/home/data/db/mysql

pass=$(cat /etc/mysql/debian.cnf |grep password |head -n 1|awk '{print $3}')

mkdir -p ./tmp
echo "GRANT ALL ON *.* TO 'debian-sys-maint'@'localhost' IDENTIFIED BY PASSWORD '"$pass"';" > ./tmp/debian_sys_maint.sql
echo use mysql >>./tmp/debian_sys_maint.sql
echo "update user set Password = password('"$pass"') where User='debian-sys-maint';" >>./tmp/debian_sys_maint.sql
echo "FLUSH PRIVILEGES;" >>./tmp/debian_sys_maint.sql

service mysql start
mysql  < ./tmp/debian_sys_maint.sql

