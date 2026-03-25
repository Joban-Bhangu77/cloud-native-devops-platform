#!/bin/bash

echo "🚀 Deploying to Kubernetes..."

kubectl set image deployment/flask-app flask-container=jobanbhangu77/flask-app:$BUILD_NUMBER

kubectl rollout status deployment flask-app
