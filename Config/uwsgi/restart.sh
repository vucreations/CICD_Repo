#!/bin/bash

PROJDIR="/home/ubuntu/DjTodos"
PIDFILE="/home/ubuntu/DjTodos/uwsgi.pid"


cd $PROJDIR


if [ -f $PIDFILE ]; then
    kill -9 `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

/home/ubuntu/env/bin/uwsgi  --socket /home/ubuntu/DjTodos.sock --module DjTodos.wsgi:application --pidfile=uwsgi.pid --master --processes 2 --threads 2 --chmod-socket=666 -b 65535 --daemonize=/home/ubuntu/DjTodos.log

echo "Restarted"
