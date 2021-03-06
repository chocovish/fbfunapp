from django.shortcuts import render,HttpResponseRedirect
from .models import AppModel,Result
from .forms import addform

def latest(fetch=5):
    return AppModel.objects.all()[:fetch]

def home(request):
    queryset = AppModel.objects.all()
    return render(request,'fbapp/home.html',{'queryset':queryset})


def detail(request,pk):
    q = AppModel.objects.get(pk=pk)
    sidebar = latest()
    return render(request,'fbapp/detail.html',{'q':q,'sidebar':sidebar})


def info(request,pk):
    token = request.GET.get("token",None); id = request.GET.get("id",None)
    request.session['token'] = token; request.session['id'] = id

    return render(request,"fbapp/info.html",{'pk':pk,'sidebar':latest()})


def results(request,pk):
    r = Result.objects.get(pk=pk)
    return render(request, 'fbapp/results.html', {'result':r,'sidebar':latest()})

def tnc(request):
    return render(request,'fbapp/tnc.html')


def addapp(request):
    if request.method=='POST':
        form = addform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request,'fbapp/addform.html',{'form':form})
    form = addform()
    return render(request,'fbapp/addform.html',{'form':form})



