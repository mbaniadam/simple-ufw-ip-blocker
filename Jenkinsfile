pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/mbaniadam/simple-ufw-ip-blocker', branch: 'main')
      }
    }

    stage('Run Container for Test') {
      steps {
        sh '''sudo docker container rm -f alpine && sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock --name alpine alpine && ls -a && sudo docker cp . alpine:



'''
      }
    }

    stage('Go to Alpine') {
      steps {
        sh '''sudo docker container exec -it alpine sh
'''
      }
    }

    stage('Test') {
      steps {
        sh ' apk add docker && apk add docker-compose && sudo docker-compose -f postgres_docker/docker-compose.yml  up -d'
      }
    }

  }
}