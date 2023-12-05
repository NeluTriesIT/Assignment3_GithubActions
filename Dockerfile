FROM python:3.9-slim

WORKDIR /app

COPY script.py /app

CMD ["python3", "./script.py"]