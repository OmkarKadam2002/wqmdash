from django.shortcuts import render, HttpResponse
import pymysql
import pandas as pd
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    connection = pymysql.connect(host='127.0.0.1', user='root', password='', database='wqm_db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sensor_readings")
    rows = cursor.fetchall()
    dataframe = pd.DataFrame(rows, columns=['ID','TURBIDITY','TEMPERATURE','PH','DATEANDTIME']) 
    return render(request, 'dashboard.html',{'dataframe': dataframe})

def get_latest_sensor_data(request):
    connection = pymysql.connect(host='127.0.0.1', user='root', password='', database='wqm_db')
    cursor = connection.cursor()
    query = "SELECT * FROM sensor_readings ORDER BY datetime DESC"
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    latest_data = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
        ]
    return JsonResponse(list(latest_data), safe=False)

def about_project(request):
    return render(request, 'about.html')
