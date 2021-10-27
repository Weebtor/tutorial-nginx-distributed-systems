# tutorial-nginx-distributed-systems

sudo ufw allow 'Nginx Full'

sudo ln -s /etc/nginx/sites-available/flaskapp.nginx /etc/nginx/sites-enabled/flaskapp.nginx
sites-available/load-balancer.nginx

gunicorn --bind 0.0.0.0:5000 flaskapp:app

service: /etc/systemd/system/flaskapp.service

## Instalación de NGINX en Windows

Para la instalación de NGINX en el sistema operativo Windows, se recomienda leer la documentación oficial alojada en el siguiente enlace. [NGINX en Windows](https://nginx.org/en/docs/windows.html)

## Instalación de NGINX en entorno Unix 

Se utiliza una distribución Ubuntu 20.04 LTS para la instalación en NGINX en un sistema operativo basado en Unix.

### Prerequisitos

El unico prerequisto existente para la instalación de NGINX es tener un usuario con acceso de privelegio a sudo.

### Instalación

NGINX se encuentra disponible en los repositorios predeterminados de Ubuntu. Por lo tanto, su instalación se puede llevar a cabo utilizando el sistema de paquetes `apt`
```bat
$ sudo apt update
$ sudo apt install nginx
```
Para comprobar la instalación, ejecutamos el comando para obtener la versión de NGINX instalada.
```bat
$ nginx -v
```
Cuando ya hemos confirmado la instalación, se puede ver el estado del servidor. Para esto debemos escribir lo siguiente:
``` bat
$ sudo systemctl status nginx
```
El resultado deberia ser similar a lo siguiente:

~~~
Output
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2021-10-25 16:08:19 UTC; 2 days ago
     Docs: man:nginx(8)
 Main PID: 2369 (nginx)
    Tasks: 2 (limit: 1153)
   Memory: 3.5M
   CGroup: /system.slice/nginx.service
           ├─2369 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2380 nginx: worker process
~~~

Finalmente para ver el servidor de NGINX en funcionamiento, se debe ingresar a la dirección:
``` bat
http://server_ip
```
Esta se puede obtener directamente en consola ingresando el siguiente comando :

``` bat
ifconfig
```

Al ingresar a la dirección mencionada, el resultado debería ser similar al siguiente:

![Resultado](https://assets.digitalocean.com/articles/nginx_1604/default_page.png)
