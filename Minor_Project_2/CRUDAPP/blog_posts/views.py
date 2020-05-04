from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import blog_posts
# Create your views here.

class blogposts(ModelForm):
    class Meta:
        model = blog_posts
        fields = '__all__'

def blog_list(request):
    context = {'blog_list': blog_posts.objects.all()}
    return render(request,"blog_posts/post_list.html",context)

# insert and update
def blog_create(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = blogposts()
        else:
            blog = blog_posts.objects.get(pk=id)
            form = blogposts(instance=blog)
        return render(request,"blog_posts/post_form.html",{'form':form})
    else:
        if id ==0:
            form = blogposts(request.POST)
        else:
            blog = blog_posts.objects.get(pk=id)
            form = blogposts(request.POST,instance=blog)
        if form.is_valid():
            form.save()
        return redirect('/blogpost/list')

def blog_delete(request, id):
    blog = blog_posts.objects.get(pk=id)
    blog.delete()
    return redirect('/blogpost/list')
