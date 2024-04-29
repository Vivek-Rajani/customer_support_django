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
                    dockerImage = docker.build('cs_docker_app_img', '-f dockerfile .')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('cs_docker_app_img').run('-d -p 8000:8000')
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
