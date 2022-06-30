


data_ingestion_dag = {
    'interval': '00 10 * * *',
    'dag_id': 'data_ingestion_dag'
}



DATASET_URL = "https://s3.amazonaws.com/nyc-tlc/trip+data/"
DATASET_FILE = "yellow_tripdata_2021-01.parquet"
PROJECT_ID = "yifan-sandbox"
BUCKET = "yifan_sandbox"
GCS_URL = "gs://yifan_sandbox"
BIGQUERY_DATASET = "sandbox_dataset"



