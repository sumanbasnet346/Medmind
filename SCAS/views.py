from django.shortcuts import render,HttpResponse
from SCAS.models import Supports
# Create your views here.
def home(request):
    allsupport = Supports.objects.all()
    return render(request,'SCAS/home.html',{'allsupport':allsupport})

def support(request,title):
    support = Supports.objects.filter(support_title=title).first()
    return render(request,'SCAS/support.html',{'support':support})