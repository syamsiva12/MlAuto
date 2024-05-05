from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return render(request, 'upload.html', {'error': 'Invalid file type'})
        
        if 'start_eda' in request.POST:
            print('eda started')
        
        # Render the DataFrame in the HTML template
        return render(request, 'display_dataframe.html', {'dataframe': df.to_html()})
    
    return render(request, 'upload.html')

def start_eda(request):
    if request.method == 'POST':
        if request.is_ajax() and request.POST.get('action') == 'start_eda':
            # Perform start EDA action
            # For example:
            # eda_results = perform_eda()
            # return JsonResponse({'success': True, 'eda_results': eda_results})
            print("success")
            return render(request, 'start_eda_result.html')
        else:
            return render(request, 'start_eda_result.html')
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request.'})