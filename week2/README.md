


# Week2 , Airflow orschestration: Orchestreate the pipeline in week1


## 1. download dataset from url
run BashOperator, and save the csv file in the given folder. 

## 2. convert csv to parquet
Benefits of parquet: Parquet stores the file schema in the file metadata. CSV files don't store file metadata, so readers need to either be supplied with the schema or the schema needs to be inferred. Supplying a schema is tedious and inferring a schema is error prone / expensive.
<https://stackoverflow.com/questions/36822224/what-are-the-pros-and-cons-of-parquet-format-compared-to-other-formats>

## 3. upload parquet to gcs

## 4. load to bigquery (BigQueryCreateExternalTableOperator)




