# 🚀 Cloud-Native DevOps Platform  
### From Code to Kubernetes — A Complete CI/CD Journey with Jenkins, Docker & AWS EKS

---

## 🌟 Introduction

In modern software engineering, delivering applications quickly and reliably is just as important as building them. Manual deployments are no longer sustainable, especially when systems need to scale and evolve continuously.

This project represents a complete, real-world implementation of a DevOps delivery pipeline, designed to automate the entire lifecycle of an application — from source code to production deployment on Kubernetes.

---

## 🧭 The Big Picture

> Every code change should automatically flow through a pipeline and become a running application 🚀


GitHub → Jenkins → Docker → DockerHub → Kubernetes (Kind → AWS EKS)


---

## 🧱 Application Overview

### 📁 app/app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps CI/CD Pipeline Running Successfully on Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
📁 requirements.txt
Flask==2.2.5
🐳 Containerization with Docker
📁 Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app/ app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]
🤖 CI/CD Pipeline with Jenkins
📁 Jenkinsfile
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "<dockerhub-username>/flask-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/YOUR_USERNAME/cloud-native-devops-platform.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
☸️ Production Deployment (Kubernetes)
📁 deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
      - name: flask-app
        image: <dockerhub-username>/flask-app
        ports:
        - containerPort: 5000
📁 service.yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  type: NodePort
  selector:
    app: flask-app
  ports:
    - port: 80
      targetPort: 5000
      nodePort: 30007
🌍 Environments (Local → Cloud)
🖥️ Local Environment
Kubernetes using Kind
Fast testing & debugging
☁️ Cloud Environment
AWS EKS (Production Ready)
Highly scalable & resilient

✔ Same configuration works everywhere
✔ No changes required

🏗️ Infrastructure as Code
Terraform
AWS (EKS, IAM, VPC)

✔ Fully automated
✔ Version controlled
✔ Reproducible

🚧 Real-World Challenges
Jenkins ↔ Kubernetes connectivity issues
Docker path issues on Windows
AWS EKS authentication debugging
CI/CD failures & retries

👉 Built strong troubleshooting mindset

🧠 Key Learnings
End-to-end CI/CD pipeline
Kubernetes deployments
Docker containerization
Infrastructure automation
Real-world debugging
🚀 Future Improvements
🔍 Prometheus & Grafana
🔐 DevSecOps (Trivy, SAST, DAST)
🔁 GitOps (ArgoCD)
📦 Helm Charts
⭐ Final Thought

This is not just a project — it’s a complete DevOps mindset.

🚀 From writing code → to running production systems — fully automated.