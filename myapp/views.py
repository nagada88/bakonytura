from django.shortcuts import render
from django.http import HttpResponse
    
from myapp.models import Entry
from django.http import HttpResponse

from .forms import PostForm

def news(request):  
    #Read ALL entries
    objects = Entry.objects.all()            
    return render(request, "news.html", {'objects': objects})
    
def trips(request):
    return
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()
        
        
    return render(request, 'post_edit.html', {'form': form})