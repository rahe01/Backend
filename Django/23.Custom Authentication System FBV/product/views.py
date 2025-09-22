from django.shortcuts import render , redirect

# Create your views here.

from django.contrib.auth.decorators import permission_required
from product.models import Product
from product.forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'list.html', {'products': products})




def product_detail(request, pk):
    product = Product.objects.get(pk=pk)  # pk diye specific product fetch
    return render(request, 'details.html', {'product': product})



@permission_required('product.add_product', raise_exception=True)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add.html', {'form': form})



@permission_required('product.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})



@permission_required('product.change_product', raise_exception=True)
def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form, 'product': product})
