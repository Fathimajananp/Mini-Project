from django.conf.urls import url
from temp import views

urlpatterns=[
    url('hom/',views.home),
    url('usr/',views.user),
    url('dly/',views.delivery),
    url('admn/',views.admin),
]