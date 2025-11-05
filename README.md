# Celery Task Queue Example

A simple example demonstrating Celery with Redis as broker/backend.

## Prerequisites

- Python 3.x
- Redis server
- Celery

## Setup

1. Install dependencies:
```bash
pip install celery redis
```

2. Start Redis server:
```bash
redis-server
```

3. Start Celery worker:
```bash
celery -A p1.main worker --loglevel=INFO
```

## Usage

Run the main script:
```bash
python p1/main.py
```

This will execute a sample task that adds two numbers asynchronously using Celery.
