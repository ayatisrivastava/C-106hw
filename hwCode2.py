import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days = []
    with open(data_path)as csv_file:
        csvreader = csv.DictReader(csv_file)
        for row in csvreader:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return{"x": marks, "y": days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation:" + correlation[0,1])

def setup():
    data_path =  'Student Marks vs Days Present.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()