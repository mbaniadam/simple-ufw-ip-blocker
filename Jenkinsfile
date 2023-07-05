pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/mbaniadam/simple-ufw-ip-blocker', branch: 'main')
      }
    }

    stage('Build') {
      steps {
        sh 'ls -a && sudo docker-compose -f postgres_docker/docker-compose.yml  up -d'
      }
    }

    stage('Docker ps') {
      steps {
        sh 'sudo docker ps'
      }
    }

  }
}