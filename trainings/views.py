from django.shortcuts import render,HttpResponse
from trainings.models import training
# Create your views here.
def home(request):
    alltrain = training.objects.all()
    return render(request,'trainings/home.html',{'alltrain':alltrain})

def trainings(request,title):
    alltrain = training.objects.filter(training_title=title).first()
    return render(request,'trainings/trainings.html',{'alltrain':alltrain})