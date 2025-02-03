from django.urls import path
from core.views import index

appname= "ShopJewely"

urlpatterns = [
    path("", index)
]
