from django.urls import path
from .views import *

urlpatterns=[
    path('add/<int:product_id>/',cart_add,name='cart_add'),
    path('',cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',cart_remove,name='cart_remove'),
    path('update/<int:product_id>/<int:quantity>/',cart_update,name='cart_update'),
]