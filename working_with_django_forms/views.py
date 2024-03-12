from django.shortcuts import render
from .forms import Userforms

global n1
global n2
global final
def check(request):
    final=0
    try:
        if request.method=='POST':
            n1=int(request.POST.get('value1'))
            n2=int(request.POST.get('value2'))
            final=n1+n2

        print(final)

        
            
    except:
        pass


    return render(request,"form.html",{'final':final})

