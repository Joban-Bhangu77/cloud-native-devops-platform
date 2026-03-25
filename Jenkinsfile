pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

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
                sh 'bash scripts/build.sh'
            }
        }

        stage('Push Docker Image') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'USER',
            passwordVariable: 'PASS'
        )]) {
            sh 'bash scripts/push.sh'
        }
    }
}

        stage('Deploy to Kubernetes') {
            steps {
                sh 'bash scripts/deploy.sh'
            }
        }
    }
}