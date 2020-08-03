from django.shortcuts import render

from .models import Phone


def show_catalog(request):
    sort_arg = request.GET.get('sort', 'name')

    all_phones = None
    if sort_arg == 'min_price':
        all_phones = Phone.objects.order_by('price')
    elif sort_arg == 'max_price':
        all_phones = Phone.objects.order_by('-price')
    else:
        all_phones = Phone.objects.order_by('name')

    template = 'catalog.html'
    context = {
        'all_phones': all_phones
    }
    return render(request, template, context)


def show_product(request, slug):
    slug_from_url = request.path.split('/')[2]
    phone = Phone.objects.get(slug__exact=slug_from_url)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
