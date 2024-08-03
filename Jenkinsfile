pipeline {
    agent any

    environment {
        // Define any necessary environment variables here
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/botlaram/devops_projects.git'
            }
        }

        stage('Set Up Python') {
            steps {
                // Use a specific Python version if necessary
                sh 'pyenv global 3.9'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Nox Session for Script') {
            steps {
                // Run the Nox session for the script
                sh 'nox -s run_script'
            }
        }

        stage('Run Nox Session for Test Cases') {
            steps {
                // Run the Nox session for the test cases
                sh 'nox -s tests'
            }
        }
    }

    post {
        always {
            // Cleanup or archive artifacts if necessary
        }
        success {
            // Actions to take upon a successful build
            echo 'Build succeeded!'
        }
        failure {
            // Actions to take upon a failed build
            echo 'Build failed!'
        }
    }
}
