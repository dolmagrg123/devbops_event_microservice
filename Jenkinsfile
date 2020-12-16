pipeline {
     agent {
        docker { image {'python:3.7.2' }
     // agent { docker { image 'python:3.7.2' } }
     // agent any
     environment {
        AWS_DEFAULT_REGION = 'us-east-1'
     }
     stages {
         stage('build') {
             steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                         sh 'pip install flask --user'
                         sh 'pip install boto3 --user'
                         sh 'pip install requests --user'

                     }
                 }
         }
         stage('test') {
             steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 test.py'
                 }
             }
         }
         stage('speak'){
             steps{
                 slackSend channel: '﻿jenkinsnotify', color: '#1eff00', message: 'The event services test has passed! '

             }

         }
     }
     }
