# tutorial-nginx-distributed-systems

sudo ufw allow 'Nginx Full'

sudo ln -s /etc/nginx/sites-available/flaskapp.nginx /etc/nginx/sites-enabled/flaskapp.nginx
sites-available/load-balancer.nginx

gunicorn --bind 0.0.0.0:5000 flaskapp:app

service: /etc/systemd/system/flaskapp.service