
FROM python:3.10-slim


RUN pip install --no-cache-dir requests beautifulsoup4 psycopg2-binary

WORKDIR /app


COPY . .


CMD ["python", "save_to_postgres.py"]
 
