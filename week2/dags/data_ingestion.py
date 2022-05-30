



import os
import logging
import common.config as cf
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq

PROJECT_ID = cf.PROJECT_ID
BUCKET = cf.BUCKET
GCS_URL = cf.GCS_URL
dataset_url = cf.DATASET_URL + cf.DATASET_FILE
BIGQUERY_DATASET = cf.BIGQUERY_DATASET
DATASET_FILE = cf.DATASET_FILE



default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}



dag_id = cf.data_ingestion_dag.get("dag_id")
interval = cf.data_ingestion_dag.get("interval")

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id=dag_id,
    schedule_interval=interval,
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['data_engineering_bootcamp'],
) as dag:

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sSL {dataset_url} > {DATASET_FILE}  && gsutil cp {DATASET_FILE} {GCS_URL}"  
    )

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "external_table",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/{DATASET_FILE}"],
            },
        },
    )

    download_dataset_task  >> bigquery_external_table_task