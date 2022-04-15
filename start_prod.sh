#!/bin/sh
if [ "$1" = "clean" ]; then
    # stop previous run and remove old containers
    docker-compose -f docker-compose.prod.yml down --rmi all
else
    # only shutdown
    docker-compose -f docker-compose.prod.yml down
fi
# build new containers and start
docker-compose -f docker-compose.prod.yml up --build -d
# stop pgadmin container (only start on demand)
./stop_pgadmin.sh
if [ "$1" = "clean" ]; then
    # do migrations
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
fi