pipeline {
    agent any

    environment {
        PYTHON_ENV = "venv"
        PYTHON_HOME = "C:\\Users\\MT\\AppData\\Local\\Programs\\Python\\Python311"
        PATH = "${PYTHON_HOME};${env.PATH}"

        // Flask settings for tests
        FLASK_ENV = "testing"
        FLASK_APP = "Backend"
        DATABASE_URL = "sqlite:///:memory:"
        ENABLE_SSL = "False"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        disableConcurrentBuilds()
        timestamps()
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                python --version
                python -m venv %PYTHON_ENV%
                call %PYTHON_ENV%\\Scripts\\activate.bat

                python -m pip install --upgrade pip
                pip install -r Backend\\requirements.txt
                """
            }
        }

        stage('Start Application (for UI Tests)') {
            steps {
                bat """
                call %PYTHON_ENV%\\Scripts\\activate.bat

                set FLASK_RUN_PORT=5000
                start /B flask run --host=0.0.0.0 --port=5000
                timeout /T 10
                """
            }
        }

        stage('Run Tests (Unit + API + UI)') {
            steps {
                bat """
                call %PYTHON_ENV%\\Scripts\\activate.bat
                pytest tests -v
                """
            }
        }

        stage('Build Docker Image') {
            when {
                expression { fileExists('Dockerfile') }
            }
            steps {
                bat """
                docker build -t helm-bridge:latest .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            when {
                expression { fileExists('k8s_deployment') }
            }
            steps {
                bat """
                kubectl apply -f k8s_deployment
                """
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Check logs for details.'
        }
    }
}
