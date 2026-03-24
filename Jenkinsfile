pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-product:latest ./app/product-service'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop flask-test || true
                docker rm flask-test || true
                docker run -d -p 5001:5000 --name flask-test flask-product:latest
                '''
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5001/products'
            }
        }
    }
}