from django.shortcuts import render
from .models import Post
import markdown
import blog.mdext

def post_list(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'bootstrap-variable-list.html', {'item': posts})

def post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        return render(request, 'bootstrap-variable.html', 
                {'title': post.title,
                 'content': markdown.markdown(post.text, extensions=['codehilite', 'fenced_code', blog.mdext.ResponsiveImg]),
                 'date': post.date})
    except:
        return render(request, 'bootstrap-variable.html',
                {'title': 'Ошибка 404',
                'content': 'Такого поста в моём блоге нет',
                'date': ''})
