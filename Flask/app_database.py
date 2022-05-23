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

now = datetime.datetime.now()
month = str(now.month)
day = str(now.day)
year = str(now.year)
today = month + "-" + day + "-" + year

#outputDirectory = str(sys.argv[1])
global outputDirectory
outputDirectory = 'C:/'
def createDirectories(outputDirectory):
    directories = [outputDirectory + "DLS/Trial-01",
                        outputDirectory + "DLS/Trial-02"

    ]

    for i in directories:
        try:
            os.chdir(i)
            print(i + " Found")
        except:
            os.makedirs(i)
            print(i + " not found. Creating " + i + " now")

    os.chdir("C:/Users/JohnPeasari/John/Flask")
    return 'Done!'
createDirectories(outputDirectory)

app = Flask(__name__,template_folder='templates')
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
def get_db_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="Varsham0803",
                                  host="localhost",
                                  port="5432",
                                  database="inventory")
    return connection

@app.route('/select')
def index():
    conn = get_db_connection()
    df = pd.read_sql('''SELECT * FROM "John".titanic_data''', conn)
    return render_template('index.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

@app.route('/plot',methods=['GET', 'POST'])
def image():
    conn = get_db_connection()
    df = pd.read_sql('''SELECT * FROM "John".titanic_data''', conn)
    plot = sns.catplot(x ="Sex", hue ="Survived",kind ="count", data = df)
    plot.savefig("static/sns_barplot.png")
    return render_template("graph.html")



if __name__ == '__main__':
    app.run(debug=True)