"""Fish_Mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('login/',include('login.url')),
    url('Meat/', include('Meat.url')),
    url('delivery/',include('delivery.url')),
    url('feedback/',include('feedback.url')),
    url('item_details/',include('item_details.url')),
    url('payment/',include('payment.url')),
    url('user/',include('user.url')),
    url('temp/',include('temp.url')),
    url('delivery_boy/',include('delivery_boy.url')),
    url('order_details/',include('order_details.url'))

]
