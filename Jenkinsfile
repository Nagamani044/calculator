pipeline {
    agent any
    stages {
        stage('Check Docker') {
            steps {
                sh 'docker ps'
            }
        }
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

        stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
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
