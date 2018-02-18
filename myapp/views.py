from django.shortcuts import render, get_object_or_404
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
            new_entry           = newsEntry()
            whattodelete        = int(newsPostForm.cleaned_data['content'])
            new_entry.content   = newsPostForm.cleaned_data['content']
            new_entry.author    = newsPostForm.cleaned_data['author']
            new_entry.date      = newsPostForm.cleaned_data['date']
            what2del = get_object_or_404(newsEntry, id=whattodelete)
            what2del.delete()
    else:
        newsPostForm = PostForm()
        
        
    return render(request, 'post_edit.html', {'newsPostForm': newsPostForm})