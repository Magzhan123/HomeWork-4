from django.shortcuts import render

#from blogApp.models import HttpResponse
from blogApp.models import Post

def postShow(request, blog_id):
	return HttpResponse("We are in post with id= %s" %blog_id )

def index(request):
    blog_id = HttpResponse.objects.order_by('-pub_date')[:5]
    context = {'blog_id': blog_id}
    return render(request, 'blogApp/index.html', context)