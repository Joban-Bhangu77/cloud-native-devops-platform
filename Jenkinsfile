pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Joban-Bhangu77/cloud-native-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jobanbhangu/flask-app:latest .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push jobanbhangu/flask-app:latest'
            }
        }
    }
}