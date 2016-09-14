#!/bin/bash

cp nginx.conf /etc/nginx/sites-available/

LINK_FILE='/etc/nginx/sites-enabled/module'

if [ -f $LINK_FILE ]; then
    rm $LINK_FILE
fi

ln -s /etc/nginx/sites-available/nginx.conf $LINK_FILE

service nginx restart

/usr/bin/uwsgi --ini markers.ini --uid root --gid www-data

