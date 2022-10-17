from django.conf.urls import url
from Meat import views

urlpatterns=[
    url('meat/',views.post),
    url('mng/',views.manage),
    url('updt/(?P<idd>\w+)',views.edit,name="ed"),
    url('delete/(?P<idd>\w+)',views.deletem,name="dlt")
]


