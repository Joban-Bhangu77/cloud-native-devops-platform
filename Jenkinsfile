pipeline {
    agent any

    options {
        skipDefaultCheckout(false)
    }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

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
                sh '''
                sleep 5
                curl http://localhost:5001/products
                docker ps
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}