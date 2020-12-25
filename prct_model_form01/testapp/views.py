from django.shortcuts import render
from testapp.models import StudModel
from testapp.forms import StudForm
# Create your views here.
def showIndex(request):
    form=StudForm()
    if request.method == "POST":
        form=StudForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/index.html',{'form':form})


def showData(request):
    items=StudModel.objects.all()
    return render(request,'testapp/showdata.html',{'items':items})    
