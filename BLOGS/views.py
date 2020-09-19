from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import Http404

# Create your views here.

from BLOGS.models import Blog, Comment
from BLOGS.forms import NewCommentForm

def index(request):
    newest_blogs = Blog.objects.order_by('created_time')[:5]

    return render(request, 'index.html', {'newest_blogs' : newest_blogs})

def detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        comments = Comment.objects.filter(blog=pk)
    except Blog.DoesNotExist:
        raise Http404('Blog does not exist')
    return render(request, 'single.html', {'blog':blog, 'comments':comments})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def new_comment(request, pk):
    blog = get_object_or_404(Blog, pk = pk)

    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
            return redirect('detail',pk =pk)
        else:

            context = {
                'blog':blog,
                'form':form,

            }
            return render(request, 'single.html', context=context)
    return redirect('detail')