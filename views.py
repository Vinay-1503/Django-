from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Vinay'})

def add(request):
        val1 =int(request.POST['num1']) # Get the value of 'num1' parameter, default to 0 if not found
        val2 = int(request.POST['num2'])  # Get the value of 'num2' parameter, default to 0 if not found
        res = val1 + val2
        return render(request, 'result.html', {'result': res})
    