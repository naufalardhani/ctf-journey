FROM php:apache
RUN apt-get update && apt-get upgrade -y


COPY src/ /var/www/html/
COPY flag.txt /flag
EXPOSE 80