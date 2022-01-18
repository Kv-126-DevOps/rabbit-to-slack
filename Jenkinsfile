pipeline {
    agent any 
    stages {
        stage('Auth & Git') { 
            steps {
                sh '''docker-credential-gcr configure-docker --registries="gcr.io" && docker-credential-gcr config --token-source="env"'''
                git branch: 'main', url: 'https://github.com/DevOps-Kv-116/rabbit_to_slack.git'
                
            }
        }
        stage('Build') { 
            steps {
                sh '''docker build -t gcr.io/${TF_VAR_project}/rabbit_to_slack .'''
            }
        }
        stage('Push') { 
            steps {
                sh '''docker push "gcr.io/${TF_VAR_project}/rabbit_to_slack"'''
            }
        }
    }
}
