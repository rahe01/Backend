from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookForm
from book.models import Book

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



def books(request):

    all_books = Book.objects.all()

    return render(request, 'book/books.html' , {'books': all_books})

def bookDetail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book/bookdetail.html' , {'book': book})

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    book.delete()