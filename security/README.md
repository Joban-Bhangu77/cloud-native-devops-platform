# 🔐 DevSecOps Security Layer

This folder contains all security integrations used in the pipeline.

## 🔍 Tools

SAST - SonarQube  
SCA - OWASP Dependency Check  
Container Security - Trivy  
DAST - OWASP ZAP  

## 🚀 Flow

Code → SAST → SCA → Build → Image Scan → Deploy → DAST
