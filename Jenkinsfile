pipeline {
    agent { docker { image 'python:3.7.2' } }
    stages {
        stage('build') {
            steps {
                   withEnv(["HOME=${env.WORKSPACE}"]) {
                        sh 'pip install flask'
                    }
                }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                   sh 'python3 test_Events.py'
                }
            }
        }
    }
}
