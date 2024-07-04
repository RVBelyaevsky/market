from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products,
               'title': 'Каталог'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User:{name}(phone number:{phone}) send message: "{message}"')

    context = {'title': 'Контакты'}

    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)
