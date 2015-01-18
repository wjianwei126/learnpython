cd /home/data/site/redmine/
bundle install --without development test
rake generate_secret_token
bundle update
rake db:migrate RAILS_ENV=production
rake tmp:cache:clear
rake tmp:sessions:clear
