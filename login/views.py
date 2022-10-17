from django.shortcuts import render
from login.models import Login
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        uname=request.POST.get("name")
        passw=request.POST.get("psw")
        obj=Login.objects.filter(username=uname,password=passw)
        tp=""
        for ob in obj:
            tp = ob.type
            lid = ob.log_id
            if tp == "admin":
                request.session["log_id"] = lid
                return render(request,'temp/admin.html')
                # return '''<script>alert("valid");window.location="temp/admin.html"</script>'''
            elif tp == "user":
                request.session["log_id"] = lid
                return render(request,'temp/user.html')
            elif tp == "deliveryboy":
                request.session["log_id"] = lid
                return render(request,'temp/delivery boy.html')
            # else:
            #     url = '/'
            #     resp_body = '<script>alert("Login successfull");\
            #                     window.location="%s"</script>' % url
            #     return HttpResponse(resp_body)

        objlist = "username or password incorrect....please try again....!"
        context = {
            'msg':objlist,
        }
        return render(request, 'login/login.html',context)
    return render(request,'login/login.html')
