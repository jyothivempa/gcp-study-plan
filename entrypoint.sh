#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files (optional for dev, needed for prod)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Start server
echo "Starting server..."
exec "$@"
