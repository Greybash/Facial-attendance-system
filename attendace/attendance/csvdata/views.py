from django.shortcuts import render
import pandas as pd
from datetime import datetime

now= datetime.now()
current_date=now.strftime("%Y-%m-%d")

    
    
def main_page(request):
    return render(request, 'csvdata/main.html')


def show_csv1_data(request):
    file_path = f'C:/Users/HP/AppData/Local/Programs/Python/Python311/attendace/{current_date}_python_final_attendance.csv'
    df = pd.read_csv(file_path)
    html_table = df.to_html(classes='table table-striped', index=False)
    return render(request, 'csvdata/table.html', {'table': html_table})


def show_csv2_data(request):
    file_path = f'C:/Users/HP/AppData/Local/Programs/Python/Python311/attendace/{current_date}_iot_final_attendance.csv'
    df = pd.read_csv(file_path)
    html_table = df.to_html(classes='table table-striped', index=False)
    return render(request, 'csvdata/table.html', {'table': html_table})

    


    
