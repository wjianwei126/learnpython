apt-get -y update
apt-get -y install curl git
curl -sSL https://get.rvm.io | bash -s stable
source /etc/profile.d/rvm.sh
apt-get -y install  bzip2 gawk g++ make libc6-dev libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev
rvm install 2.1
rvm use 2.1
ruby -v
rvm use 2.1 --default

wget -qP ./packages/ http://production.cf.rubygems.org/rubygems/rubygems-2.4.0.tgz
tar zxf ./packages/rubygems-2.4.0.tgz
cd rubygems-2.4.0
mkdir -p lib/rubygems
mkdir -p /usr/local/rvm/rubies/ruby-2.1.2/lib/ruby/site_ruby/2.1.0/rubygems
ruby setup.rb
cd ..
mv rubygems-2.4.0 /tmp
gem sources --remove https://rubygems.org/
gem sources -a http://ruby.taobao.org/
