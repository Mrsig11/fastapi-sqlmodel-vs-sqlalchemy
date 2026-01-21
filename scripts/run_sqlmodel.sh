#!/bin/bash

export ORM_ENGINE=sqlmodel

echo "🚀 Starting Todo API with SQLModel..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
