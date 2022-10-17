from django.conf.urls import url
from delivery_boy import views

urlpatterns=[
    url('delivery_boy/',views.post),
]