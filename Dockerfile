FROM debian:latest

MAINTAINER Haoran He

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /var/www/devbops_event_microservice/requirements.txt
RUN pip install -r /var/www/devbops_event_microservice/requirements.txt

# Apache config file
COPY ./flaskapp.conf /etc/apache2/sites-available/flaskapp.conf
RUN a2ensite flaskapp
RUN a2enmod headers

# wsgi config file Mod_wsgi
COPY ./flaskapp.wsgi /var/www/devbops_event_microservice/flaskapp.wsgi

####################
COPY ./devbops_event_microservice /var/www/devbops_event_microservice/devbops_event_microservice

RUN a2dissite 000-default.conf
RUN a2ensite flaskapp.conf

#### LINK LOGS
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

EXPOSE 80
WORKDIR /var/www/devbops_event_microservice

CMD  /usr/sbin/apache2ctl -D FOREGROUND
