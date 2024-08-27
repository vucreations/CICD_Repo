#!/bin/bash

PROJDIR="/home/ubuntu/CI-CD-TestRepo"
PIDFILE="/home/ubuntu/CI-CD-TestRepo/uwsgi.pid"


cd $PROJDIR


if [ -f $PIDFILE ]; then
    kill -9 cat -- $PIDFILE
    rm -f -- $PIDFILE
fi

/home/ubuntu/env/bin/uwsgi  --socket /home/ubuntu/CI-CD-TestRepo.sock --module DjTodos.wsgi:application --pidfile=uwsgi.pid --master --processes 2 --threads 2 --chmod-socket=666 -b 65535 --daemonize=/home/ubuntu/CI-CD-TestRepo.log

echo "Restarted"