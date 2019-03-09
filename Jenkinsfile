pipeline {
  agent {
    docker {
      image 'doc-service'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh '''echo "Run unit-tests:"
sh "mkdir -p results"
sh "pwd"
sh "docker-compose --project-name doc-service build test"
sh "docker run doc-service_test:latest"'''
      }
    }
  }
}