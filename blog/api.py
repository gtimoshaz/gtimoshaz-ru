from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from blog.models import Post
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def post_with_files(request):
    if "POST" == request.method:
        for f in request.FILES.values():
            fn = f.name
            with open(f'static/{fn}', 'wb+') as fd:
                for chunk in f.chunks():
                    fd.write(chunk)
    text = request.POST.get('text', '')
    title = text.split("\n")[0]
    text = "\n".join(text.split("\n")[1:])
    short = text.split("<cut>")[0]
    text = "".join(text.split("<cut>"))
    post = Post(text=text, short=short, title=title)
    post.save()
    return HttpResponse('Uploaded')

