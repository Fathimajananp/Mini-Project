from django.shortcuts import render
from delivery.models import Delivery
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Delivery()
        obj.time=request.POST.get('time')
        obj.status=request.POST.get('sts')
        obj.save()
    return render(request, 'delivery/delivery.html')

