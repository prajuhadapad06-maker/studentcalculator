pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Student Calculator Checkout'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Student Calculator'
            }
        }

        stage('Test') {
            steps {
                bat 'python --version'
            }
        }

        stage('Success') {
            steps {
                echo 'Pipeline completed successfully!'
            }
        }
    }
}