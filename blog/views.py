from django.shortcuts import render
from .models import Post
from .forms import MsgForm
# Create your views here.
def home(request):
    if request.method=='GET':
        form = MsgForm()
        form=MsgForm(request.GET)
        if form.is_valid():
            form.save()
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts,'form':form})
