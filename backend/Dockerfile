FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

COPY .. /app/

# Stage 2: Production image
FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /install /usr/local

COPY .. /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
