#!/bin/bash

export ORM_ENGINE=sqlalchemy

echo "🚀 Starting Todo API with SQLAlchemy..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
