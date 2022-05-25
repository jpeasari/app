import os
import sys
import datetime
import time
import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import shutil
import matplotlib
matplotlib.use('Agg')
from sqlalchemy import create_engine
app = Flask(__name__,template_folder='templates')

def get_db_connection():
    engine = create_engine('postgresql+psycopg2://postgres:Varsham0803@localhost/inventory')
    connection = engine.connect()
    print("Database connection estaablished !!")
    return connection

def close_db_connection(connection):
    close = connection.close()
    return close
    

@app.route('/select')
def index():
    conn = get_db_connection()
    df = pd.read_sql('''SELECT * FROM "John".titanic_data''', conn)
    return render_template('index.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

@app.route('/plot',methods=['GET', 'POST'])
def image():
    conn = get_db_connection()
    df = pd.read_sql('''SELECT * FROM "John".titanic_data''', conn)
    close_db_connection(conn)
    plot = sns.catplot(x ="Sex", hue ="Survived",kind ="count", data = df)
    plot.savefig("static/sns_barplot.png")
    return render_template("graph.html")




if __name__ == '__main__':
    app.run(debug=True)
