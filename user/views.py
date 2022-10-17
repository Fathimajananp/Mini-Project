from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Login()
        obj.username=request.POST.get('nme')
        obj.password=request.POST.get('psd')
        obj.type='user'
        obj.save()


        ob=User()

        ob.gender=request.POST.get('gn')
        ob.email=request.POST.get('email')
        ob.house_name=request.POST.get('adrs')
        ob.place=request.POST.get('place')
        ob.city=request.POST.get('cty')
        ob.pin_code=request.POST.get('pin')
        ob.phone_no=request.POST.get('phno')
        ob.log_id=obj.log_id
        ob.save()
    return render(request,'user/user.html')

def view(request):
    ob=User.objects.all()
    context={
        'objval':ob
    }
    return render(request,'user/view customers.html',context)

def manage(request):
    ss=request.session["log_id"]
    ob=User.objects.filter(log_id=ss)
    context={
        'objval':ob
    }
    return render(request,'user/edit.html',context)

def edit(request,idd):
    ob=User.objects.get(c_id=idd)
    context={
        'objval':ob
    }
    if request.method=='POST':
        ob=User.objects.get(c_id=idd)

        ob.gender=request.POST.get('gn')
        ob.email=request.POST.get('email')
        ob.house_name=request.POST.get('adrs')
        ob.place=request.POST.get('place')
        ob.city=request.POST.get('cty')
        ob.pin_code=request.POST.get('pin')
        ob.phone_no=request.POST.get('phno')

        ob.save()

        # url='/temp/hom/'
        # resp_body='<script>alert("profile updated successfully");\
        # window.location="%s"</script>' % url
        # return HttpResponse(resp_body)

    return render(request,'user/edit profile.html',context)

def deletec(request,idd):
    obj=User.objects.get(c_id=idd).delete()
    return manage(request)
