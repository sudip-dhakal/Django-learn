from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# from .forms import Userforms


def check(request):
    data={}
    final=0
    try:
        if request.method=='GET':
            n1=int(request.GET.get('value1'))
            n2=int(request.GET.get('value2'))
            finalans=n1+n2

            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }

            print(final)
            url="/thanks?final={}".format(final)
            return HttpResponseRedirect(url)

        
            
    except:
        pass


    return render(request,"form.html",data)


def thankyou(request):
    if request.method=="GET":
        output1=request.GET.get('final')
    return render(request,"thanks.html",{'final':output1})

