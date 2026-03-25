#!/bin/bash

echo "🚀 Building Docker Image..."

docker build -t jobanbhangu77/flask-app:$BUILD_NUMBER .

echo "✅ Build Completed"
