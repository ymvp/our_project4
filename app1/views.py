from django.shortcuts import render

# Create your views here.
def operations(request):
    data= 100
    d={'a':data}
    return render (request,'operation.html',d)