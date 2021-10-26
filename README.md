# tutorial-nginx-distributed-systems

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
