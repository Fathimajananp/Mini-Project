from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.
def post(request):
    if request.method=='POST':
        obj=Feedback()
        obj.feedback=request.POST.get('Feedback')
        obj.date=request.POST.get('dte')
        obj.o_id=1
        obj.save()
    return render(request, 'feedback/feedback.html')

