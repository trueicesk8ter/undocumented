import pandas as pd
from pandas.io import sql
import sqlalchemy
import os

def load_into_sql(path):
    engine = sqlalchemy.create_engine('mysql://user:pass@host/database')
    for root, dirs, files in os.walk(path, topdown=False):
         for name in files:
            if ".csv" in name:
                csv_to_read = f'{root}/{name}'
                print(csv_to_read)
                try:
                    a = pd.read_csv(csv_to_read,sep='\t', nrows = 3000)
                    table_name = name[:-4]
                    a.to_sql(con=engine, name=table_name, if_exists='replace' )
                except:
                    a = pd.read_csv(csv_to_read,sep='\t+', nrows = 3000)
                    table_name = name[:-4]
                    a.to_sql(con=engine, name=table_name, if_exists='replace' )

load_into_sql("file")
