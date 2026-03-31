#!/bin/bash

echo "Starting SCA Scan..."

dependency-check.sh \
--project "DevSecOps Project" \
--scan . \
--format HTML \
--out reports/

echo "SCA Scan Completed"
