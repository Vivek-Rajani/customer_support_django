pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vivek-Rajani/customer_support_django'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build('cs_docker_app_img', '-f /app/customer_support_project/dockerfile .')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker image ls'
                    sh 'docker run -d -p 8000:8000 cs_docker_app_img'
                }
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -af'
        }
    }
}
