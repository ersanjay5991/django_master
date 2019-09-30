from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'welcome to my tutorails', 'number':200}
    return render(request,'django_url/index.html', context_dict)

def other(request):
    return render(request, 'django_url/other.html')

def relative(request):
    return render(request,'django_url/relative-url.html')