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
        sh 'cd postgres_docker'
      }
    }

    stage('Docker') {
      steps {
        sh 'docker-compose up '
      }
    }

  }
}