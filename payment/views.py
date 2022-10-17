from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def post(request):
    if request.method=='POST':
        ob=Payment()
        ob.o_id=1
        ob.date=request.POST.get('date')
        ob.mode_of_payment=request.POST.get('pmt')
        ob.amount=request.POST.get('amt')
        ob.status=request.POST.get('sts')
        ob.save()

    return render(request,'payment/payment.html')
