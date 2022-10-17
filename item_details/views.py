from django.shortcuts import render
from item_details.models import ItemDetails
# Create your views here.
def post(request):
    if request.method=='POST':
        ob=ItemDetails()
        ob.m_id=1
        ob.image=request.POST.get('img')
        ob.status=request.POST.get('sts')
        ob.save()
    return render(request,'item_details/item details.html')
