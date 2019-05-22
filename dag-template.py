from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators import python_operator 
from airflow.contrib.operators import dataproc_operator
from airflow.operators.python_operator import PythonOperator
from airflow.utils import trigger_rule
import datetime
#import os

PYSPARK_JOB = 'gs://panw-dataproc-demo/wordcount.py'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'airflow_demo2',
    default_args=default_args,
    description='Orchestration DAG',
    schedule_interval=timedelta(days=1), 
)

# t1, t2 and t3 are examples of tasks created by instantiating operators\

t1 = dataproc_operator.DataprocClusterCreateOperator(
        task_id='create_dataproc_cluster',
        # ds_nodash is an airflow macro for "[Execution] Date string no dashes"
        # in YYYYMMDD format. See docs https://airflow.apache.org/code.html?highlight=macros#macros
        cluster_name='panw-dp-cluster',
        region='global',
        zone='us-central1-b',
        metadata={'gcs-connector-version':'1.9.11','bigquery-connector-version':'0.13.11'},
        num_workers=2,
        init_actions_uris=['gs://dataproc-initialization-actions/connectors/connectors.sh'],
        image_version='1.3',
        storage_bucket='panw-dataproc-demo',
        project_id='gcptraining-17042017',
        dag=dag,
        
    )

t2 = dataproc_operator.DataProcPySparkOperator(
        task_id='run_wordcount_job',
        main=PYSPARK_JOB,
        cluster_name='panw-dp-cluster',
        region='global',
        dag=dag,
  
    )

t3 = dataproc_operator.DataprocClusterDeleteOperator(
        task_id='delete_dataproc_cluster',
        project_id='gcptraining-17042017',
        cluster_name='panw-dp-cluster',
        # Setting trigger_rule to ALL_DONE causes the cluster to be deleted
        # even if the Dataproc job fails.
        trigger_rule=trigger_rule.TriggerRule.ALL_DONE,
        dag=dag,

    )

t1 >> t2 >> t3

#--replace tag if you want to replace the schema in table
#bq --location=[LOCATION] load --[no]replace [DATASET].[TABLE] [PATH_TO_SOURCE] [SCHEMA]
