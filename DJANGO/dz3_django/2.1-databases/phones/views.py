from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort", 'name')
    if 'min_price' in sort:
        sort = 'price'
    if 'max_price' in sort:
        sort = '-price'
    context = {'phones': [phone.__dict__ for phone in Phone.objects.all().order_by(sort)]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug).__dict__}
    return render(request, template, context)
