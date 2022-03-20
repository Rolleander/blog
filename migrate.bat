call docker-compose exec web pipenv run python manage.py flush --no-input
call docker-compose exec web pipenv run python manage.py migrate