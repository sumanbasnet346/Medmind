from django.shortcuts import render,HttpResponse
from guidelines.models import guidelist
# Create your views here.
def home(request):
    allguide = guidelist.objects.all()
    return render(request,'guidelines/home.html',{'allguide':allguide})

    

def guide(request,title):
    guide = guidelist.objects.filter(guide_title=title).first()
    return render(request,'guidelines/guide.html',{'guide':guide})