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
        sh '''sudo docker container rm -f alpine && sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock --name alpine alpine && ls -a && sudo docker cp . alpine:/tmp

'''
      }
    }

    stage('Test on Alpine') {
      steps {
        sh 'sudo docker container exec alpine  apk add docker docker-compose python3 py3-pip && sudo docker-compose -f postgres_docker/docker-compose.yml up -d && sudo docker ps'
      }
    }

  }
}