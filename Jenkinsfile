pipeline {
    agent any
    stages {
        stage('trigger-airflow-dag') {
            steps {
                sh 'gsutil -q stat gs://panw-dataproc-demo/wordcount.py || gsutil cp wordcount.py  gs://panw-dataproc-demo/'
                sh 'gsutil rm gs://panw-dataproc-demo/wordcount.py'
                sh 'gsutil cp wordcount.py gs://[anw-dataproc-demo/'
            }
        }
    }
