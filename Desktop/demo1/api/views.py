from django.shortcuts import render
# Create your views here.

from django.http.response import HttpResponse, JsonResponse

def hello(request):
    return HttpResponse('<h1>Hello msg</h1>')


products = []
for i in range(5):
    products.append(
        {
            'id': i,
            'name': f'product {i}',
            'price': i * 100
        }
    )
def product_list(request):
    return JsonResponse(products, safe = False)

def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'ochibka':'producta ne suchestvuet'})

def category_list():
    pass

def category_detail(request, category_list):
    pass
def category_products(request, category_list):
    pass

