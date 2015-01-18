echo "CREATE DATABASE redmine CHARACTER SET utf8;" >./tmp/redmine_db.sql
mysql  < ./tmp/redmine_db.sql

echo "GRANT ALL PRIVILEGES ON redmine.* TO 'redmine'@'localhost' IDENTIFIED BY 'EDCnO0Qgsc' WITH GRANT OPTION;" >./tmp/redmine_user.sql
echo "FLUSH PRIVILEGES;" >>./tmp/redmien_user.sql
mysql  < ./tmp/redmine_user.sql
