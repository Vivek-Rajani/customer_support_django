pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vivek-Rajani/customer_support_django'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python manage.py test'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build('cs_docker_app_img', '.')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    bat 'docker image ls'
                    bat 'docker run -d -p 8000:8000 cs_docker_app_img'
                }
            }
        }
    }
    
    post {
        always {
            bat 'docker system prune -af'
        }
    }
}
