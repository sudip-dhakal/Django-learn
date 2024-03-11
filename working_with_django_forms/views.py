from django.shortcuts import render
from .forms import Userforms




data={}
final=0
fn=Userforms()
n1=0
n2=0
def check(request):
    try:
        if request.method=='POST':
            n1=int(request.POST.get['value1'])
            n2=int(request.POST.get['value2'])
            final=n1+n2

        data={
            'first':n1,
            'second':n2,
            'output':final,
            'formdata':fn,
        }
        
            
    except:
        pass



    return render(request,"form.html",{'formdata':fn})

print(n1+n2)


def thankyou(request):
    return render(request,"thanks.html",{'sum':final})
