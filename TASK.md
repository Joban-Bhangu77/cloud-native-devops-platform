# 📋 TASK.md — Cloud-Native DevOps Platform Execution Guide

---

## 🎯 Objective

This file provides a step-by-step checklist to implement the complete Cloud-Native DevOps pipeline.

👉 Full practical guide:
https://medium.com/@jobanjitsinghamritsar/from-code-to-kubernetes-building-a-complete-ci-cd-pipeline-with-jenkins-docker-kubernetes-80c59327b683

---

## ✅ TASK CHECKLIST

### 🧭 Setup Environment
- [ ] Install Git  
- [ ] Install Docker  
- [ ] Install kubectl  
- [ ] Install kind  
- [ ] Install eksctl  
- [ ] Install AWS CLI  

---

### 📦 Clone Repository
- [ ] Clone the project
```bash
git clone https://github.com/YOUR_USERNAME/cloud-native-devops-platform.git
cd cloud-native-devops-platform
```

---

### 🐳 Build & Push Docker Image
- [ ] Build Docker image
```bash
docker build -t <dockerhub-username>/flask-app .
```

- [ ] Login to DockerHub
```bash
docker login
```

- [ ] Push Docker image
```bash
docker push <dockerhub-username>/flask-app
```

---

### ☸️ Local Kubernetes Deployment (Kind)
- [ ] Create cluster
```bash
kind create cluster --name devops-cluster
```

- [ ] Deploy application
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

- [ ] Verify
```bash
kubectl get pods
kubectl get svc
```

- [ ] Access app
```bash
kubectl port-forward service/flask-service 8080:80
```

---

### 🤖 Jenkins Setup
- [ ] Run Jenkins
```bash
docker run -d -p 8081:8080 -p 50000:50000 jenkins/jenkins:lts
```

- [ ] Configure pipeline  
- [ ] Connect GitHub repo  
- [ ] Run pipeline  

---

### ☁️ AWS EKS Deployment
- [ ] Create cluster
```bash
eksctl create cluster --name devops-cluster --region us-east-1
```

- [ ] Deploy app
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

- [ ] Verify
```bash
kubectl get nodes
kubectl get pods
kubectl get svc
```

---

## 🚀 Final Goal

- [ ] Application deployed locally  
- [ ] Application deployed on AWS  
- [ ] CI/CD pipeline working  
- [ ] End-to-end automation complete  

---

## ⭐ Note

Follow tasks step-by-step and verify each stage before moving forward.

This ensures smooth execution and real-world understanding of DevOps workflows.
