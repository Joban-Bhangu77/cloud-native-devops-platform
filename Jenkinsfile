pipeline {
    agent any

    environment {
        IMAGE_NAME = "jobanbhangu/flask-app"
        TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Joban-Bhangu77/cloud-native-devops-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'jobanjitsinghamritsar@gmail.com',
                    passwordVariable: 'Bhangu12345!'
                )]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$TAG'
            }
        }
    }
}