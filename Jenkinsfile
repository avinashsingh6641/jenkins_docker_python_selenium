pipeline {
    agent any
    tools {
        git 'git'  // Use the name you set in the Git section
    }

    stages {
        stage('Checkout Git Repo') {
            steps {
                git 'https://github.com/avinashsingh6641/jenkins_docker_python_selenium.git'
            }
        }

        stage('Prepare Docker Build Context') {
            steps {
                // Copy requirements.txt and tests into the docker build folder
                sh '''
                cp requirements.txt /jenkins-docker/test_runner/requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-selenium-runner /jenkins-docker/test_runner'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                script {
                    def parallelContainers = [:]
                    for (int i = 1; i <= 2; i++) {
                        def idx = i
                        parallelContainers["Container-${idx}"] = {
                            sh """
                            docker run --rm -v ${env.WORKSPACE}/tests:/tests python-selenium-runner pytest /tests
                            """
                        }
                    }
                    parallel parallelContainers
                }
            }
        }
    }
}
