pipeline {
    agent any

    stages {

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