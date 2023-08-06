from django.urls import path
from .views import goods

urlpatterns = [
    path('goods/', goods, name='goods'),

]