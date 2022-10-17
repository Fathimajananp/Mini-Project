from django.conf.urls import url
from user import views

urlpatterns=[
    url('user/',views.post),
    url('view/',views.view),
    url('edit/',views.edit),
    url('mange/',views.manage),
    url('update/#b(?P<idd>\w+)',views.edit,name="update"),
    url('delete/(?P<idd>\w+)',views.deletec,name="delet")
]