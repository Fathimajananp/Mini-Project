from django.shortcuts import render
from delivery_boy.models import DeliveryBoy
from login.models import Login
# Create your views here.

def post(request):
    if request.method=='POST':
        ob=Login()
        ob.username=request.POST.get('name')
        ob.password=request.POST.get('psd')
        ob.type='deliveryboy'
        ob.save()


        obj=DeliveryBoy()

        obj.email_id=request.POST.get('email')
        obj.address=request.POST.get('address')
        obj.phone_no=request.POST.get('phno')
        obj.status=request.POST.get('sts')
        obj.log_id=ob.log_id
        obj.save()
    return render(request,'delivery_boy/delivery boy.html')