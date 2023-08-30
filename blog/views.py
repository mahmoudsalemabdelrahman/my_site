from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts':posts})



def post_detail(request, year, month, day, post):

    #method 1
    #try:
        #post =Post.objects.git(id=id)
    #except post.DoesNotExist:
        #raise Http404("No Post Found.")
    #return render(request, 'blog/post/detail.html',{'post':post})

    # method 2
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug = post,
                             publish__year= year,
                             publish__month = month, 
                             publish__day = day

                             )
    return render(request, 'blog/post/detail.html',{'post':post})

