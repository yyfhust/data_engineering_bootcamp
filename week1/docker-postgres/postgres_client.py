#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import argparse
from time import time
import os


def main(args):
    user = args.user
    password = args.password
    host = args.host 
    port = args.port 
    db = args.db
    table_name = args.table_name
    url = args.url
    csv_name = 'output.csv'
    os.system( "wget {url} -O {csv_name}".format(url = url, csv_name = csv_name) )

    engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{db}'.format( user = user, password = password, host = host, port = port, db=db ))

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)




    while True: 
        
        start = time()
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime =pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        end = time()
        print("insert another chunk, took %.3f s" %(end-start))
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='load CSV data to Postgres')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')
    args = parser.parse_args()
    main(args)