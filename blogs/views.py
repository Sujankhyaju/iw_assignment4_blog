from django.shortcuts import render, redirect,get_object_or_404 , reverse

from .models import Blogs , Author

from .forms import CreatePostForm

# Create your views here.
def home_view(request):
    data = Blogs.objects.all().order_by('title')[:3]
    recent = Blogs.objects.order_by('-published_date')[:2]
    authors = Author.objects.all().order_by('name')
    context = {
        'data':data,
        'authors':authors,
        'recent_blog':recent
        
    }

    return render(request,'blogs/index.html',context=context)

def post_view(request):
    posts = Blogs.objects.all().order_by('-published_date')
    
    context = {
        'posts':posts
        
    }
    return render(request,'blogs/blog.html', context=context)


def blog_detail(request,blog_id):
    blog_object = get_object_or_404(Blogs,id=blog_id)
    context = {
        'blog_object':blog_object
    }

    return render(request,'blogs/blog_detail.html',context=context)

def create_view(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            form.save()
            return redirect('/blogs/index.html')
        else:
            print('form is invalid')

    else:
        form = CreatePostForm()


    return render(request,'blogs/create_blog.html', context={'form':form})

def author_view(request):

    data = Author.objects.all().order_by('name')
    context = {
        'data':data
    }
    return render(request,'blogs/author_list.html', context=context)

def base_view(request):
    return render(request, 'blogs/base_blog.html',{})