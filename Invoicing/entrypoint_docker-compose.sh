#!/bin/bash

# Wait until the database service is ready
while !</dev/tcp/invoice-generator-postgres-container/5432; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Apply Django migrations #
python manage.py makemigrations
python manage.py migrate
python manage.py migrate invoice1  # If 'invoice1' app has migrations

# Create Django superuser if not already created
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin') if not User.objects.filter(username='admin').exists() else None"

# Start the Django development server
exec "$@"
