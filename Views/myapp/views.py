from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound , HttpResponseRedirect

# Create your views here.

# - Simple plain text RESPONSE
def demo1(request):
    return HttpResponse("Hello World! This is my first Django view.")


# - Number RESPONSE
def demo2(request):
    return HttpResponse(1000)



# - Boolead RESPONSE
def demo3(request):
    return HttpResponse(None)


# - JSON RESPONSE
def demo4(request):
    
    data={
        "name":"John",
        "age":30,
        "city":"New York"
    }
    
    
    
    return JsonResponse(data)





# - Not Found
def demo5(request):
    return HttpResponseNotFound("<h1>404 Not Found</h1><p>The requested resource was not found on this server.</p>")







# - Redirect
def demo6(request):
    return HttpResponseRedirect("/")







# - With status code
def demo7(request):
    return HttpResponse("This is a custom status code response.", status=500)






# - With RESPONSE header
def demo8(request):
    
    response = HttpResponse("Hello world" )
    response["Custom-Header"] = "ABC123"
    response["Developer"] = "Rahe"
    response["token"] = "XYZ987"
    response["Access-Control-Allow-Origin"] = "*"
    return response






# - With RESPONSE cookies
def demo9(request):
    return HttpResponse("This is a response with cookies.")

