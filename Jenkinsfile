pipeline {
    agent {
        docker {
            image 'python:3.10' // Replace with your preferred image
            args '-u root'      // Optional: run as root if needed
        }
    }

    environment {
        APP_NAME = 'calculator'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'
            }
        }

        stage('Build') {
            steps {
                echo "Building $APP_NAME..."
                // Add build steps here if applicable
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying $APP_NAME..."
                // Add deployment steps here if needed
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
    }
}
