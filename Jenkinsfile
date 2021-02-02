node {
    stage("Github Checkout"){
        git credentialsId: 'git', url: 'https://github.com/dolmagrg123/devbops_event_microservice'
       
    }
    stage("Testing python"){
        
      
    }
    stage("Docker Build Image"){
        sh 'docker build -t dolmagrg123/event .'
    }
    stage("Push Docker Image"){
        withCredentials([string(credentialsId: 'DockerHub', variable: 'DockerHub')]) {
            sh "docker login -u dolmagrg123 -p${DockerHub}"
    }
        sh 'docker push dolmagrg123/event'
    }
    stage ("Run container in EC2"){
        def dockerRm = 'docker rm -f app_event'
        def dockerRmI = 'docker rmi dolmagrg123/event'
        def dockerRun = 'docker run -p 8092:80 -d --name app_event dolmagrg123/event'
        sshagent(['dev-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.76 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.76 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.76 ${dockerRun}"
  
        }
       
        
       
    }
}
    
