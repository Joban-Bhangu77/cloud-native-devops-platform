#!/bin/bash

TARGET_URL=$1

if [ -z "$TARGET_URL" ]; then
  echo "❌ Provide target URL"
  exit 1
fi

echo "🌐 Starting DAST Scan on $TARGET_URL"

MSYS_NO_PATHCONV=1 docker run -t \
-v "$(pwd):/zap/wrk" \
zaproxy/zap-stable zap-baseline.py \
-t $TARGET_URL \
-r zap-report.html

echo "✔ DAST Scan Completed"
