call docker-compose exec web pipenv run python manage.py makemigrations
call docker-compose exec web pipenv run python manage.py migrate