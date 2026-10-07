FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_ENV=production

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Static files are baked into the image and served by WhiteNoise.
# collectstatic only needs settings to import, so dummy values are fine here.
RUN DJANGO_SECRET_KEY=build POSTGRES_DB=x POSTGRES_USER=x POSTGRES_PASSWORD=x \
    python manage.py collectstatic --noinput \
 && chmod +x entrypoint.sh \
 && useradd --create-home --uid 1000 app \
 && chown -R app:app /usr/src/app
USER app

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "blogwebsite.wsgi", "--bind", "0.0.0.0:8000", "--workers", "2", "--access-logfile", "-"]
