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
        sh 'docker-compose -f postgres_docker/docker-compose.yml  up '
      }
    }

  }
}