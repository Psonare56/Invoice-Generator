#!/bin/sh

# Apply database migrations
python manage.py makemigrations
python manage.py migrate
python manage.py migrate invoice1

# Create Django superuser
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin') if not User.objects.filter(username='admin').exists() else None"

# Start the Django server
exec "$@"
