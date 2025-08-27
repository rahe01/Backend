from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the myapp index.")



# Method GET , PUT , POST , PATCH, DELETE
@csrf_exempt
def demo1(request):
    if request.method == 'POST':
        return HttpResponse("Hello World, This is demo1 Post Method")
    elif request.method == 'GET':
        return HttpResponse("This is demo1 GET Method")
    elif request.method == 'PUT':
        return HttpResponse("This is demo1 PUT Method")
    elif request.method == 'PATCH':
        return HttpResponse("This is demo1 PATCH Method")
    elif request.method == 'DELETE':
        return HttpResponse("This is demo1 DELETE Method")
    else:
        return HttpResponse("Method not allowed", status=405)





# Method with URL Query string
def demo2(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    city = request.GET.get("city")
    return HttpResponse(name + " " + age + " " + city)




# Method with request header
def demo3(request):
    token1 = request.headers.get("token")
    return HttpResponse(token1) 

   


# Method POST with request body JSON
@csrf_exempt
def demo4(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponse(data['name'])
        
 



# Method POST with request From Data
@csrf_exempt
def demo5(request):
    if request.method == 'POST':
        data =request.POST.dict()
        return JsonResponse(data)
        
        




# Multipart from data upload
@csrf_exempt
def demo6(request):
    if request.method == 'POST':
       uploaded_file = request.FILES.get('myfile')
       with open(f"uploads/{uploaded_file.name}" , "wb" ) as myFile:
           for EachChunk in uploaded_file.chunks():
               myFile.write(EachChunk)
       return HttpResponse("File uploaded successfully")          
    




# Catch request Cookies
def demo7(request):
    return HttpResponse("Demo7")