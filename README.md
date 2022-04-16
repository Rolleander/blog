# rol-ost.de blog
Repository for developing my homepage &amp; blog

Runs on: Django, Tailwind CSS, Summernote, Gunicorn, Nginx, PostgreSQL, Alpine 

Build with: pipenv &amp; Docker

## Install development environment

1. Create environment file in project folder .env.dev:

```
CLEANSTART=1
DEBUG=1
SSL=0
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=*
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_dev
SQL_USER=django_dev
SQL_PASSWORD=django_dev
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

2. Start tailwind dev process

Execute start_tailwind_dev.bat

3. Start the docker containers

```
docker-compose up --build
```

The page is reachable via http over port 8000 and Pgadmin is available on port 5050

## Install production environment

1. Create environment file in project folder .env.prod and fill out remaining settings:

```
CLEANSTART=1
DEBUG=0
SSL=1
SECRET_KEY= ...
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] .your-domain
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=production
SQL_USER= ...
SQL_PASSWORD= ...
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

2.  Create environment file for database .env.prod.db and fill out remaining settings:

```
POSTGRES_USER= ...
POSTGRES_PASSWORD= ...
POSTGRES_DB=production
PGADMIN_DEFAULT_EMAIL= ...
PGADMIN_DEFAULT_PASSWORD= ...
```

3. Put ssl private and public key in /nginx folder and update the filenames in /nginx/Dockerfile:

```
FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY YOUR_SSL_CERTIFICATE /etc/nginx/cert.cer
COPY YOUR_SSL_PRIVATE_KEY /etc/nginx/key.key
```

4. Start the docker containers

```
docker-compose -f docker-compose.prod.yml up --build
```

The page is reachable over ssl (port 443), http requests to port 80 are redirected to https. Pgadmin is available on port 5050
