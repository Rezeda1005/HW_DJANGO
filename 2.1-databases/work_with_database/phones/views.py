from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    sort = request.GET.get("sort", "")

    if (sort == 'min_price'):
        phone = Phone.objects.order_by('price')
    elif (sort == 'price'):
        phone = Phone.objects.order_by('-price')
    elif (sort == 'name'):
        phone = Phone.objects.order_by('name')
    else:
        phone = Phone.objects.all()

    context = {'phone': phone}
    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug )
    print(phone.name)
    context = {'phone': phone}
    return render(
        request,
        'product.html',
        context
    )