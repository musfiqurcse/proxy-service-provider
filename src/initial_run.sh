python manage.py makemigrations configuration --settings=proxy_service_provider.settings.core
python manage.py migrate --settings=proxy_service_provider.settings.core
python manage.py runserver --settings=proxy_service_provider.settings.core