pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Tests') {
      steps {
        sh 'venv/bin -c "pytest"'
      }
    }
  }
}