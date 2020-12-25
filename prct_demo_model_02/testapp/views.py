from django.shortcuts import render
from testapp.models import EmpModel
from testapp.forms import EmpForm
# Create your views here.
def showIndex(request):
    form=EmpForm()
    if request.method =="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'testapp/index.html',{'form':form})
def showData(request):
    items=EmpModel.objects.all()
    return render(request,'testapp/showdata.html',{'items':items})