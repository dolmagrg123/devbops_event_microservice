node{
    
    stage('GitHub Checkout'){
        git branch: 'master', credentialsId: 'git-creds', url: 'https://github.com/dolmagrg123/devbops_event_microservice'
    }
    
    stage('DevBops Event Test'){
        sh 'python3 test_Events.py'
    }
    
    stage('Docker Image Build'){
        sh 'docker build -t dolmagrg123/devbops_event .'
    
    }

    stage('Docker Image Push'){

        withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
            sh "docker login -u dolmagrg123 -p ${dockerHubPwd}"
    
            }
        
        sh 'docker push dolmagrg123/devbops_event'
    
    }

    stage('Run Docker Container on Private EC2'){
        def dockerRm = 'docker rm -f app_event'
        def dockerRmI = 'docker rmi dolmagrg123/devbops_event'
        def dockerRun = 'docker run -p 8092:80 -d --name app_event dolmagrg123/devbops_event'
        sshagent(['docker-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRun}"
           
        }
    
    }   
}
