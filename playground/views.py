from itertools import product
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order

def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    #     pass

    # exists = Product.objects.filter(pk=0).exists()

    # queryset = Product.objects.filter(unit_price=20)

    # queryset = Product.objects.filter(unit_price__gt=20)

    # queryset = Product.objects.filter(unit_price__range=(20, 30))

    # queryset = Product.objects.filter(collection__id__range=(4,5))

    # queryset = Product.objects.filter(title__icontains='coffee')

    # queryset = Product.objects.filter(last_update__year=2021)

    # queryset = Product.objects.filter(description__isnull=True)


    # Products: inventory < 10 AND unit_price < 20
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # Products: inventory < 10 OR unit_price < 20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20))

    # Products: inventory < 10 AND NOT unit_price < 20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20))


    # Reference Fields
    # Products: inventory = unit_price
    # queryset = Product.objects.filter(inventory=F('unit_price'))

    # SORT
    # queryset = Product.objects.order_by('unit_price', '-title')

    # LIMITING RESULTS
    # queryset = Product.objects.all()[5:10]

    # SELECTING FIELDS TO QUERY --> DICTIONARY
    # queryset = Product.objects.values('id', 'title', 'collection__title')

    # SELECTING FIELDS TO QUERY --> TUPLES
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')


    ### EX. SELECT PRODUCTS THAT HAVE BEEN ORDERED AND SORTED BY TITLE
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product__id').distinct()
    # ).order_by('title')


    # DEFERRING FIELDS --> LOT OF QUERIES
    # queryset = Product.objects.only('id', 'title')

    # DEFERRING FIELDS
    # queryset = Product.objects.defer('description')
    
   
    # SELECTING RELATED OBJECTS
    # select_related (1)
    # prefetch_related (n)
    # queryset = Product.objects.select_related('collection').all()


    ### EX. GET THE LAST 5 ORDERS WITH THEIR CUSTOMER AND ITEMS (INCLUDE PRODUCT)
    queryset = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]



    context = {
        "name": "Ciro",
        "orders": list(queryset)
    }

    return render(request, "hello.html", context)
