

# 1. Create postgres docker instance

```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

# 2. install CLI client 

```
pip install pgcli
```

# 3. connect to the database
```
pgcli -h localhost -p 5432 -U root -d ny_taxi
```

# 4. download data
```
wget https://s3.amazonaws.com/nyc-tlc/csv_backup/yellow_tripdata_2021-01.csv

# count number of lines 
wc -l yellow_tripdata_2021-01.csv 

# preview
less yellow_tripdata_2021-01.csv  

```


# 5. install pgadmin
```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```
pgadmin cannot connect to postgres since they are hosted in two different containers (networks)
solution is to run them in the same network 
```
docker network create pg-network
```

then rerun postgres and pgadmin
```
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v $(pwd)/ny_taxi:/var/lib/postgresql/data -p 5432:5432 --network="pg-network" --name pg-database postgres:13
```

```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-2 \
  dpage/pgadmin4
```



# 6. dockerize the ingestion code (in jupyternotebook)
```
jupyter nbconvert --to=script postgres_client.ipynb


RUN:
python3 postgres_client.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=https://s3.amazonaws.com/nyc-tlc/csv_backup/yellow_tripdata_2021-01.csv

```


Build the image : 
```
docker build -t taxi_ingest:v001 .

```

```
docker run -it --network=pg-network taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \     ## pay attention, cannot use locahost here. 
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=https://s3.amazonaws.com/nyc-tlc/csv_backup/yellow_tripdata_2021-01.csv


```


# 7. docker compose

```
docker-compose up ## with -d : detached mode  

docker-compose down ## shut down
```







