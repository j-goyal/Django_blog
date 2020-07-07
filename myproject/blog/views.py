from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allposts = Post.objects.all()               # pull all objects from Post model
    context = {'allposts':allposts}
    return render(request, 'blog/blogHome.html',context)
    

def blogPost(request, slug):
    #return HttpResponse(f'this is blog post : {slug}')

    post = Post.objects.filter(slug=slug)[0]            # find slug which should be unique to each blog
    post.views = post.views + 1
    post.save(0)
    
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context)

