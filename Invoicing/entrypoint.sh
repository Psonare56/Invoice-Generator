#!/bin/sh

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create Django superuser
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None"

# Start the Django server
exec "$@"
