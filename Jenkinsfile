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
                    docker.build('cs_docker_app_img:latest', '.')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "comp314passwordtemp" | docker login -u Vivek100 --password-stdin
                bat 'docker push cs_docker_app_img:latest'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('cs_docker_app_img:latest').pull()
                    docker.image('cs_docker_app_img:latest').run('-d -p 8000:8000 --name cs_docker_container')
                }
            }
        }
    }
}
