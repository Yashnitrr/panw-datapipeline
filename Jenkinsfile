pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'gsutil cp -r . gs://shopin-continuous-integration-data'
            }
        }
    }
