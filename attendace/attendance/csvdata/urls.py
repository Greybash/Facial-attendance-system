from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),  # Main page
    path('PYTHON ATTENDANCE/', views.show_csv1_data, name='PYTHON ATTENDANCE'),  # CSV 1 page
    path('IOT ATTENDANCE/', views.show_csv2_data, name='IOT ATTENDANCE'),  # CSV 2 page
    
    # Add more paths for additional CSVs
]
