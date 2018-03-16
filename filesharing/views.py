from django.shortcuts import render

# Create your views here.
def remoteConnection(request):
    return render(request, 'CloudBridge/index.html')