


airflow_bucket="gs://us-central1-composer-sandbo-700e0a4c-bucket"

gsutil -o 'GSUtil:parallel_process_count=1' -m cp -r dags "${airflow_bucket}"
