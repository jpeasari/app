import sys
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


inventoryfilelocation = "inventory.csv"
inventory = pd.read_csv(inventoryfilelocation)
print(inventory.head)

# engine = create_engine('postgresql+psycopg2://postgres:Varsham0803@localhost/inventory')

def get_db_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="Varsham0803",
                                  host="localhost",
                                  port="5432",
                                  database="inventory")
    cursor = connection.cursor()

    return cursor
cursor = get_db_connection()


def Initialize(inventoryfilelocation,database):
    success = False
    inventory = pd.read_csv(inventoryfilelocation)
    engine = create_engine('postgresql+psycopg2://postgres:Varsham0803@localhost/inventory')
    try:
        inventory.to_sql(name="ExperimentInventory", con = engine, if_exists = 'append',index=False)
        success = True
        database.close()
        
    except Exception as e:
        print(str(e))
        # database.CloseConnection()
        print('Database connection error !!')
        #raise DatabaseError
    return success


Initialize(inventoryfilelocation, cursor)