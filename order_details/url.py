from django.conf.urls import url
from order_details import views

urlpatterns=[
    url('order_details/',views.viewm),
    url('booking/(?P<idd>\w+)',views.post),
    url('viewadmin/',views.viewa),
    url('status/(?P<idd>\w+)',views.status,name="st"),
    url('sts/',views.views)
]