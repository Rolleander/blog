#!/bin/sh
# stop previous run and remove old containers
docker-compose -f docker-compose.prod.yml down --rmi all
# build new containers and start
docker-compose -f docker-compose.prod.yml up --build -d