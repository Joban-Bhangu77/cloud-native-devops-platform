#!/bin/bash

echo "🚀 Pushing Docker Image..."

docker push jobanbhangu77/flask-app:$BUILD_NUMBER

echo "✅ Push Completed"
