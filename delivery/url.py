from django.conf.urls import url
from delivery import views

urlpatterns=[
    url('del/',views.post),
]