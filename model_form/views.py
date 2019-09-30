from django.shortcuts import render

# Create your views here.

from .forms import  Newuserform
# Create your views here.
def index(request):
    return render(request,'model_form/index.html')

def data_view(request):
    form =Newuserform()

    if request.method == "POST":
        form = Newuserform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(' Error in from ')
    return render(request,'model_form/form.html', {'form':form})