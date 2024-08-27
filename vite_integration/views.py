from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("Hello World, CICD Pipeline with manual approval mail test..")
