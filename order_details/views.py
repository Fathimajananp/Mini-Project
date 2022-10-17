from django.shortcuts import render
from order_details.models import OrderDetails
from Meat.models import Meats
import datetime
# Create your views here.

def viewm(request):
    ob = Meats.objects.all()
    context = {
        'objval': ob
    }
    return render(request,'order_details/view order.html',context)

def post(request,idd):
    ss=request.session["log_id"]
    if request.method=='POST':
        obj=OrderDetails()
        obj.m_id=idd
        obj.c_id=ss
        obj.delivery_date=request.POST.get('date')
        obj.date=datetime.datetime.today()
        obj.choosen_quantity=request.POST.get('qnty')
        obj.save()
    return render(request,'order_details/booking.html')


def viewa(request):
    ob = OrderDetails.objects.all()
    context = {
        'objval': ob
    }
    return render(request,'order_details/view admin.html',context)

def status(request,idd):
    if request.method=='POST':
        ob=OrderDetails.objects.get(o_id=idd)
        ob.status=request.POST.get('sts')
        ob.save()
        return viewa(request)
    return render(request,'order_details/status.html')

def views(request):
    ob = OrderDetails.objects.all()
    context = {
        'objval': ob
    }
    return render(request,'order_details/view status.html',context)