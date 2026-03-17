pipeline {
    agent any

    stage('Checkout') {
    steps {
        git branch: 'main', url: 'https://github.com/Joban-Bhangu77/cloud-native-devops-platform.git'
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