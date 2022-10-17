from django.conf.urls import url
from item_details import views

urlpatterns=[
    url('item_details/',views.post)
]