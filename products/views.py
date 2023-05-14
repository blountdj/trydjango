from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product


def product_list_view(request):
    queryset = Product.objects.all() # returns list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


# ORIGINAL
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # re-render form
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# FOR HTML BASED FORMS (BAD IDEA!)
# def product_create_view(request):
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=3)
    # context = {
    #     'title': obj.title,
    #     'desription': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
