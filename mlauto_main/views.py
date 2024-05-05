from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
# Create your views here.

def app_level(request):
    return render(request, 'home.html')
    
def start_project(request):
    return render(request,'start_project.html')

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
            print(df.head())
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
            print(df.head())
        else:
            return render(request, 'upload.html', {'error': 'Invalid file type'})
        # Do something with the DataFrame (e.g., save to database)
        return render(request, 'upload.html', {'success': 'File uploaded successfully'})
    return render(request, 'upload.html')