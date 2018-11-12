from django.shortcuts import render
from .models import linedata
from django.http import HttpResponse
def insert(request):
    id=int(request.GET['a'])
    name=request.GET['b']
    Vr=int(request.GET['c'])
    Vy = int(request.GET['d'])
    Vb = int(request.GET['e'])
    Ir1 = int(request.GET['f'])
    Iy1 = int(request.GET['g'])
    Ib1 = int(request.GET['h'])
    pow = int(request.GET['i'])
    ene1 = int(request.GET['j'])
    f=linedata(cust_id=id,cust_name=name,voltage_R=Vr,voltage_B=Vb,voltage_Y=Vy,Ir=Ir1,Iy=Iy1,Ib=Ib1,power=pow,energy_consumption=ene1)
    f.save()
    return HttpResponse("<html> <body> request submitted </body> </html>")
def display(request):
    recs=linedata.objects.all()
    return render(request,'display.html',{'records':recs})
def home(reuqest):
    return  render(reuqest,'home.html')

