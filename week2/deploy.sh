


airflow_bucket="gs://us-east1-gfp-e88fa259-bucket"

gsutil -o 'GSUtil:parallel_process_count=1' -m cp -r  "${airflow_bucket}/dags"  "${airflow_bucket}/dags.last"
gsutil -o 'GSUtil:parallel_process_count=1' -m cp -r dags "${airflow_bucket}"
