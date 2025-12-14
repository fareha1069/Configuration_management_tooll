pipeline {
    agent any

    environment {
        // Define environment variables
        PYTHON_ENV = "venv"
        PYTHON_PATH = "C:\Users\MT\AppData\Local\Programs\Python\Python311\python.exe"
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
                // Create virtual environment and install dependencies
                bat """
                PYTHON_PATH -m venv %PYTHON_ENV%
                call %PYTHON_ENV%\\Scripts\\activate.bat
                PYTHON_PATH -m pip install --upgrade pip
                pip install -r Backend\\requirements.txt || exit 0
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call %PYTHON_ENV%\\Scripts\\activate.bat
                pytest tests
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t myapp:latest .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat """
                kubectl apply -f k8s_deployment\\
                """
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
