from django.shortcuts import render


from .forms import Formname

# Create your views here.
def index(request):
    return render(request,'django_form/index.html')

def form_view(request):
    form = Formname()

    if request.method == 'POST':
        form = Formname(request.POST)

        if form.is_valid():
            print("form is valid")
            print("name :"+ form.cleaned_data['name'])
            print("email :"+form.cleaned_data['email'])
            print("text :"+form.cleaned_data['text'])

    return render(request,'django_form/form.html',{'form': form})