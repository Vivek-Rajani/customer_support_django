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
                    def dockerfile = 'dockerfile'
                    def imageTag = "vivek100/cs_docker_app_img" 
                    customImage = docker.build(imageTag, "-f ${dockerfile} ./")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'comp314') {
                        customImage.push()
                    }
                }
            }
        }

        stage('Tomcat Deployment of Docker Container') {
            steps {
                script {
                    def tomcatContainerName = "cs_docker_tomcat_app_${BUILD_ID}"
                    customImage.run('-p 8080:8080 -d --name ' + tomcatContainerName)
                }
            }
        }
    }
}
