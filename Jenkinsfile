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
                    dockerImage = docker.build('cs_docker_app_img')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    dockerImage.inside('-p 8000:8000') {
                        sh 'docker run -d -p 8000:8000 cd_docker_app_img'
                    }
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
