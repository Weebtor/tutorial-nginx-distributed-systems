# tutorial-nginx-distributed-systems

sites-available/load-balancer.nginx

gunicorn --bind 0.0.0.0:5000 flaskapp:app

service: /etc/systemd/system/flaskapp.service