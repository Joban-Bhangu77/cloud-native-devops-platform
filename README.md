# 🚀 Cloud-Native DevOps Platform  
### From Code to Kubernetes — A Complete CI/CD Journey with Jenkins, Docker & AWS EKS

---

## 🌟 Introduction

In modern software engineering, delivering applications quickly and reliably is just as important as building them. Manual deployments are no longer sustainable, especially when systems need to scale and evolve continuously. This project represents a complete, real-world implementation of a **DevOps delivery pipeline**, designed to automate the entire lifecycle of an application — from source code to production deployment on Kubernetes.

Rather than treating tools as isolated components, this project focuses on how they come together to form a cohesive system. By integrating Jenkins, Docker, Kubernetes, AWS EKS, and infrastructure automation, this setup mirrors the way modern cloud-native applications are deployed in production environments.

---

## 🧭 The Big Picture

At the core of this project lies a simple but powerful idea: every code change should automatically flow through a pipeline and become a running application without manual intervention.

GitHub → Jenkins → Docker → DockerHub → Kubernetes (Kind → AWS EKS)


This flow represents a continuous delivery system. Code is committed to GitHub, Jenkins detects the change and triggers a pipeline, Docker builds a container image, and Kubernetes deploys the updated application. The same workflow is used across both local and cloud environments, ensuring consistency from development to production.

---

## 📂 Repository Structure

The repository is organized to reflect how real-world systems are structured, separating application logic, infrastructure, and automation.

cloud-native-devops-platform/
├── app/
├── docker/
├── kubernetes/
├── terraform/
├── monitoring/
├── scripts/
├── jenkins/
├── Dockerfile
├── Jenkinsfile
├── deployment.yaml
├── service.yaml
├── ingress.yaml
└── requirements.txt


Each directory plays a specific role, making the project easier to maintain, scale, and understand.

---

## 🧱 Building the Application

The application itself is intentionally simple — a lightweight Flask service. The goal is not to build a complex backend, but to demonstrate how an application moves through a DevOps pipeline.

### 📁 app/app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps CI/CD Pipeline Running Successfully on Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

Once the image is built, it is pushed to DockerHub. This allows Kubernetes to pull the image and deploy it in any environment.   
    

🤖 Automating Everything with Jenkins

Jenkins acts as the brain of the system. It continuously watches the repository and triggers the pipeline whenever changes are detected. This eliminates manual steps and ensures that every update is deployed in a consistent manner.

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

This pipeline connects all layers of the system, transforming code into a deployed application automatically.

☸️ Running on Kubernetes

Kubernetes is responsible for running and managing the application containers. It ensures that the application is always available, scalable, and resilient.

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

These configurations define how the application is deployed and exposed to users.

🌍 From Local to Cloud (Kind → AWS EKS)

One of the key strengths of this project is the ability to run the same application in different environments. Initially, the application is deployed on a local Kubernetes cluster using Kind, allowing for quick testing and debugging.

Once validated, the same configuration is used to deploy the application on AWS EKS. This transition demonstrates how real-world systems move from development environments to production without changing the core logic.

🏗️ Infrastructure as Code

Instead of manually configuring cloud resources, infrastructure is defined using code. Tools like CloudFormation and Terraform are used to provision Kubernetes clusters, networking, and IAM roles.

This approach ensures that infrastructure is consistent, repeatable, and version-controlled, which is a fundamental principle in DevOps.

🚧 Challenges and Real-World Debugging

Building this system was not just about connecting tools — it involved solving real engineering problems. Issues such as Jenkins failing to communicate with Kubernetes, Docker path inconsistencies on Windows, and authentication challenges with AWS EKS required deep troubleshooting.

These challenges provided valuable insights into how systems interact across layers and reinforced the importance of understanding the underlying architecture.

🧠 What This Project Teaches

This project goes beyond basic tutorials and provides hands-on experience in designing and operating a complete DevOps system. It demonstrates how automation, containerization, orchestration, and cloud infrastructure come together to create a scalable and reliable deployment pipeline.

🚀 Future Improvements

While the current system is fully functional, it can be extended further by integrating monitoring tools like Prometheus and Grafana, adopting GitOps practices with ArgoCD, and enhancing security through automated vulnerability scanning.

⭐ Final Thought

This project represents more than just a pipeline — it reflects the mindset of modern DevOps engineering, where automation, scalability, and reliability are built into every stage of the system.