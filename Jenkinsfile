pipeline {
    agent any

    environment {
        AWS_CREDENTIALS = credentials('awscredentials') // Use the credentials ID you created in step 3
        PATH = "/usr/bin/python3:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Run Script') {
            steps {
                script {
                    sh 'pip install boto3'  // Install boto3 if not already installed
                    sh 'python3 lambda_functions_report.py'
                }
            }
        }
    }
}
