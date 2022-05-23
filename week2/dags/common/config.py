


data_ingestion_dag = {
    'interval': '00 10 * * *',
    'dag_id': 'data_ingestion_dag'
}



DATASET_URL = "https://s3.amazonaws.com/nyc-tlc/csv_backup/"
DATASET_FILE = "yellow_tripdata_2021-01.csv"
PROJECT_ID = ""
BUCKET = ""
BIGQUERY_DATASET = ""
AIRFLOW_HOME = ""