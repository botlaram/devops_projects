pipeline {
    agent any

    // Removed empty environment block

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                 git branch: 'jenkins-github-nox-pytest', url: 'https://github.com/botlaram/devops_projects.git'
            }
        }

        stage('Set Up Python') {
            steps {
                // Ensure pyenv is available and set the Python version
                sh '''
                if command -v pyenv > /dev/null; then
                    pyenv global 3.9
                else
                    echo "pyenv is not installed. Please install pyenv or use another method to set Python version."
                    exit 1
                fi
                '''
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
            // Actions to take in all cases
            echo 'Cleaning up...'
        }
        success {
            // Actions to take upon a successful build
            echo 'Build succeeded!'
        }
        failure {
            // Actions to take upon a failed build
            echo 'Build failed!'
            // Add any necessary failure handling steps here
        }
    }
}
