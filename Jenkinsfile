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
        sh '''sudo docker container rm -f dockertest && sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/jenkins/workspace/simple-ufw-ip-blocker_main:/tmp --name dockertest alpine
'''
      }
    }

    stage('Test on Alpine') {
      steps {
        sh '''sudo docker container exec dockertest apk add docker-compose python3 py3-pip && sudo docker ps
'''
      }
    }

  }
  triggers {
    githubPush()
  }
}