from django.shortcuts import render
from .models import AppModel,Result


def home(request):
    queryset = AppModel.objects.all()
    return render(request,'fbapp/home.html',{'queryset':queryset})


def detail(request,pk):
    q = AppModel.objects.get(pk=pk)
    return render(request,'fbapp/detail.html',{'q':q})


def info(request,pk):
    token = request.GET.get("token",None); id = request.GET.get("id",None)
    request.session['token'] = token; request.session['id'] = id

    return render(request,"fbapp/info.html",{'pk':pk})


def results(request,pk):
    r = Result.objects.get(pk=pk)
    return render(request, 'fbapp/results.html', {'result':r})







