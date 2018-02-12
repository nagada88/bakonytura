from django.shortcuts import render
from django.http import HttpResponse
    
from myapp.models import newsEntry
from django.http import HttpResponse

from .forms import PostForm

def news(request):  
    #Read ALL entries
    newsObjects = newsEntry.objects.all()            
    return render(request, "news.html", {'newsObjects': newsObjects})
        
def post_new(request):
    if request.method == "POST":
        newsPostForm = PostForm(request.POST)
        if newsPostForm.is_valid():
            post = newsPostForm.save(commit=False)
            post.save()
    else:
        newsPostForm = PostForm()
        
        
    return render(request, 'post_edit.html', {'newsPostForm': newsPostForm})