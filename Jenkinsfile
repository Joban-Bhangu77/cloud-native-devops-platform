pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jobanbhangu77/flask-app"
        TAG = "v1.${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Joban-Bhangu77/cloud-native-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'bash build.sh'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'bash push.sh'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'bash deploy.sh'
            }
        }
    }
}