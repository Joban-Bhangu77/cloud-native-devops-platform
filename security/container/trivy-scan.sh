#!/bin/bash

IMAGE_NAME=$1

if [ -z "$IMAGE_NAME" ]; then
  echo "❌ Provide image name"
  exit 1
fi

echo "🔍 Scanning Docker Image: $IMAGE_NAME"

MSYS_NO_PATHCONV=1 docker run --rm \
-v /var/run/docker.sock:/var/run/docker.sock \
ghcr.io/aquasecurity/trivy:latest image \
--severity HIGH,CRITICAL \
--exit-code 1 \
$IMAGE_NAME

echo "✔ Scan Completed"
