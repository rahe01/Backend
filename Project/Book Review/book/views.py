from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm

# Create your views here.


def home(request):
    return render(request, 'book/home.html')




def addBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'book/home.html')
    else:
        form = BookForm()
    return render(request, 'book/addform.html' , {'form': form})