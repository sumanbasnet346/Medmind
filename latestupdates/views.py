from django.shortcuts import render,HttpResponse,redirect
from latestupdates.models import Post
from django.contrib import messages

# Create your views here.
def updateshome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'latestupdates/home.html',context)

def updatespost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.save()
    # comments=Comment.objects.filter(post=post,parent=None)
    # replies=Comment.objects.filter(post=post).exclude(parent=None) #This means parent !=none
    # repDict = {}
    # for reply in replies:
    #     if reply.parent.sno not in repDict.keys():
    #         repDict[reply.parent.sno] = [reply]
    #     else:
    #         repDict[reply.parent.sno].append(reply)

    context = {'post':post}#,'comments':comments,'user':request.user,'repDict':repDict}
    return render(request,'latestupdates/post.html',context)

