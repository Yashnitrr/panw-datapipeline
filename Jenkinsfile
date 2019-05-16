pipeline {
    agent any
    stages {
        stage('trigger-airflow-dag') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=/home/yash_agrawal/key.json'
                sh 'gsutil -q stat gs://panw-dataproc-demo/wordcount.py || gsutil cp wordcount.py  gs://panw-dataproc-demo/'
                sh 'gsutil rm gs://panw-dataproc-demo/wordcount.py'
                sh 'gsutil cp wordcount.py gs://panw-dataproc-demo/'
                sh 'gsutil -q stat gs://us-central1-demo-2f091aed-bucket/dags/dag-template.py || gsutil cp dag-template.py gs://us-central1-demo-2f091aed-bucket/dags/'
                sh 'gsutil rm gs://us-central1-demo-2f091aed-bucket/dags/dag-template.py'
                sh 'gsutil cp dag-template.py gs://us-central1-demo-2f091aed-bucket/dags/'
            }
        }
    }
}
