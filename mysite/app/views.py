from django.shortcuts import render

# Create your views here.
def index(request):
    
    args = {
        'name': 'Jhon', 
        'age': '21', 
        'vip': 'true', 
    }
    
    return render(request, './app/index.html', args)