pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/Joban-Bhangu77/cloud-native-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-product:latest ./app/product-service'
            }
        }

        stage('Run Container (Test)') {
            steps {
                sh 'docker run -d -p 5001:5000 flask-product:latest'
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5001/products'
            }
        }
    }
}