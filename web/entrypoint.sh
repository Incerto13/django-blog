#!/bin/sh
# Container entrypoint: wait for Postgres, migrate, seed once, then run the server.
# (The old script called docker-compose from inside the container, which can't work.)
set -e

python - <<'PY'
import os, sys, time
import psycopg
dsn = dict(host=os.environ.get('DB_HOST', 'localhost'), port=os.environ.get('DB_PORT', '5432'),
           dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'],
           password=os.environ['POSTGRES_PASSWORD'], connect_timeout=3)
for attempt in range(60):
    try:
        psycopg.connect(**dsn).close()
        break
    except psycopg.OperationalError:
        print('waiting for postgres...', flush=True)
        time.sleep(2)
else:
    sys.exit('postgres never became reachable')
PY

python manage.py migrate --noinput

# Seed the demo content (2 users, 16 posts) only on an empty database.
if [ "$(python manage.py shell --no-imports -c 'from blog.models import Post; print(Post.objects.exists())')" = "False" ]; then
    echo "seeding demo content"
    python manage.py loaddata seed.json
fi

exec "$@"
