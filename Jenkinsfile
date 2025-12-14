pipeline {
    agent any

    environment {
        // Define any environment variables you need
        PYTHON_ENV = "venv"
    }

    options {
        // Keep only the last 10 builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        // Prevent concurrent builds
        disableConcurrentBuilds()
    }

    triggers {
        // Trigger build on GitHub push
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                // Pull code from GitHub
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Install dependencies
                sh '''
                python3 -m venv $PYTHON_ENV
                source $PYTHON_ENV/bin/activate
                pip install --upgrade pip
                pip install -r Backend/requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source $PYTHON_ENV/bin/activate
                pytest tests
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t myapp:latest .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s_deployment/
                '''
            }
        }
    }

    post {
        always {
            // Clean workspace after build
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
