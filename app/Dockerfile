# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev nodejs npm

# copy project
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
# RUN pipenv lock --clear
RUN pipenv install

# Install tailwind
WORKDIR /usr/src/app/theme/static_src
RUN npm i
WORKDIR /usr/src/app

# run entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]