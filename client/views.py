from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    
def client_list(request):
    return render(request, "client_list.html")
