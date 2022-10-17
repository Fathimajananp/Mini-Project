from django.shortcuts import render
from Meat.models import Meats
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Meats()
        obj.meat_name=request.POST.get('name')
        obj.items=request.POST.get('it')
        obj.type=request.POST.get('typ')
        obj.quantity=request.POST.get('qt')
        obj.price_kg=request.POST.get('amt')
        obj.image=request.POST.get('img')
        obj.status=request.POST.get('sts')
        obj.date_meat=request.POST.get('dte')
        obj.save()
    return render(request, 'Meat/Meat.html')


def manage(request):
    ob=Meats.objects.all()
    context={
        'objval':ob
    }
    return render(request,'Meat/manage meats.html',context)

def edit(request,idd):
    ob=Meats.objects.get(m_id=idd)
    context={
        'obj':ob,
    }
    if request.method=='POST':
        obj=Meats.objects.get(m_id=idd)
        obj.meat_name=request.POST.get('name')
        obj.items=request.POST.get('it')
        obj.type=request.POST.get('typ')
        obj.quantity=request.POST.get('qt')
        obj.price_kg=request.POST.get('amt')
        obj.image=request.POST.get('img')
        obj.status=request.POST.get('sts')
        obj.date_meat=request.POST.get('dte')
        obj.save()
        return manage(request)
    return render(request, 'Meat/edit.html',context)


def deletem(request,idd):
    ob=Meats.objects.get(m_id=idd).delete()
    return manage(request)

