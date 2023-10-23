pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // You may need to configure your SCM checkout here if it's not the default
                // For example, for Git:
                // checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/shonevarkey/lambda-functions-report.git']]])
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    try {
                        // Install Python and required packages if not already installed
                        sh 'pip install boto3'

                        // Run the Python script
                        sh 'python lambda_functions_report.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Failed to run the Python script: ${e.message}")
                    }
                }
            }
        }
    }

    post {
        failure {
            // Handle failure, if needed
        }
    }
}
