#!groovy

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
                    sudo docker.build('cs_docker_app_img:latest', '.')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sudo docker.withRegistry('', 'comp314') {
                        sudo docker.image('cs_docker_app_img:latest').push('latest')
                    }
                }
            }
        }


        stage('Deploy') {
            steps {
                script {
                    suduo docker.image('cs_docker_app_img:latest').pull()
                    sudo docker.image('cs_docker_app_img:latest').run('-d -p 8000:8000 --name cs_docker_container')
                }
            }
        }
    }
}
