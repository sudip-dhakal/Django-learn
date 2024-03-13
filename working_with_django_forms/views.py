from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# from .forms import Userforms


def check(request):
    data={}
    finalans=0
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

            
            return HttpResponse(finalans)

        
            
    except:
        pass

    return render(request,"form.html",data)


def thankyou(request):
    if request.method=='GET':
        output=request.GET['final']
        print(output)
        return render(request,'thanks.html',{'output':output})
    
    

