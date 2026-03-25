#!/bin/bash

echo "🔐 Logging into DockerHub..."

echo $PASS | docker login -u $USER --password-stdin

echo "🚀 Pushing Docker Image..."

docker push jobanbhangu77/flask-app:$BUILD_NUMBER

echo "✅ Push Completed"