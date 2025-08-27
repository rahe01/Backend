from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    return HttpResponse("Demo3") 

   

# Method POST with request body JSON
def demo4(request):
    return HttpResponse("Demo4")



# Method POST with request From Data
def demo5(request):
    return HttpResponse("Demo5")




# Multipart from data upload
def demo6(request):
    return HttpResponse("Demo6")




# Catch request Cookies
def demo7(request):
    return HttpResponse("Demo7")