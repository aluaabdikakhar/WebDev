from django.urls import path

from api.views import hello, product_list, product_detail

from api.views import category_list, category_detail, category_products

urlpatterns = {
    path('hello/', hello),
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:id>/', category_detail),
    path('categories/<int:id>/products/', category_products)

}