from turtle import title
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models import Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem

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


    ## Products: inventory < 10 AND unit_price < 20
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    ## Products: inventory < 10 OR unit_price < 20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20))

    # Products: inventory < 10 AND NOT unit_price < 20
    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20))


    # # REFERENCE FIELDS
    # # Products: inventory = unit_price
    # queryset = Product.objects.filter(inventory=F('unit_price'))

    # # SORT
    # queryset = Product.objects.order_by('unit_price', '-title')

    # # LIMITING RESULTS
    # queryset = Product.objects.all()[5:10]

    # # SELECTING FIELDS TO QUERY --> DICTIONARY
    # queryset = Product.objects.values('id', 'title', 'collection__title')

    # # SELECTING FIELDS TO QUERY --> TUPLES
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')


    # ## EX. SELECT PRODUCTS THAT HAVE BEEN ORDERED AND SORTED BY TITLE
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product__id').distinct()
    # ).order_by('title')


    # # DEFERRING FIELDS --> LOT OF QUERIES
    # queryset = Product.objects.only('id', 'title')

    # # DEFERRING FIELDS
    # queryset = Product.objects.defer('description')
    
   
    # # SELECTING RELATED OBJECTS
    # # select_related (1)
    # # prefetch_related (n)
    # queryset = Product.objects.select_related('collection').all()


    # ## EX. GET THE LAST 5 ORDERS WITH THEIR CUSTOMER AND ITEMS (INCLUDE PRODUCT)
    # queryset = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]


    # # AGGREGATING OBJECTS
    # result = Product.objects.filter(collection__id=4).aggregate(
    #     count=Count('id'), 
    #     min_price=Min('unit_price'))

    # # ANNOTATING OBJECTS
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F('id') + 1)

    # # CALLING DATABASE FUNCTIONS
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    # # GROUPING DATA GROUPING DATA
    # queryset = Customer.objects.annotate(
    #     order_count=Count('order')
    # )

    # # WORKING WITH EXPRESSION WRAPPERS
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # # QUERYING GENERIC RELATIONSHIPS
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    # # CUSTOM MANAGER
    # TaggedItem.objects.get_tags_for(Product, 1)


    # # UNDERSTANDING QUERYSET CACHE
    # queryset = Product.objects.all()
    # list(queryset)
    # queryset[0]

    # # CREATING OBJECTS
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # # collection.featured_product_id = 1
    # collection.save()

    # # CREATING OBJECTS (2)
    # collection = Collection.objects.create(
    #     title='Video Games',
    #     featured_product_id=1
    # )

    # # UPDATING OBJECTS
    # collection = Collection.objects.get(pk=12)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # # UPDATING OBJECTS (2)
    # Collection.objects.filter(pk=12).update(featured_product=None)


    context = {
        "name": "Ciro",
        # "products": list(queryset),
        # "orders": list(queryset),
        # "result": result,
        # "result": list(queryset)

    }

    return render(request, "hello.html", context)
