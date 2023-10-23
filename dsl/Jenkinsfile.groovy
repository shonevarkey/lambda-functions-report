pipeline {
    agent {
        docker {
            image 'python:3.8' // Replace with the appropriate Python version
        }
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'pip install boto3'
                sh 'python lambda_functions_report.py'
            }
        }
    }
}
