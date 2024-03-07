FROM php:apache
RUN apt-get update && apt-get upgrade -y
RUN apt install -y iputils-ping 


COPY src/ /var/www/html/
COPY flag /flag
EXPOSE 80