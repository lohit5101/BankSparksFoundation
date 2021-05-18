from django.shortcuts import render,redirect
from django.contrib import messages
from .models import customer,Transact
from django.http import HttpResponse, HttpResponseRedirect

gettname='vbh'
custid=-1
custid2=-1
ammt=''
ammmt=''
tempid1=""
tempid2=""
def home(request):
    return render(request,"index.html")
def transfer(request):
     if request.method == "POST":
        amt= request.POST['amt']
        rec= request.POST["rec"]
        sen=request.POST["get"]
        customers = customer.objects.all()
        global ammt
        ammt=amt

        for x in customers:
            if x.name==sen:
                global custid2
                global custid
                global tempid1
                global tempid2
                global ammmt
                if x.amount< int(amt):

                    custid2=-1
                    custid=-1
                    tempid1=x.name
                    ammmt=x.amount
                    messages.info(request, 'Insufficient Balance')

                elif int(amt)<=0:

                    custid2 = -1
                    custid = -1
                    tempid1 = x.name
                    ammmt = x.amount
                    messages.info(request, 'Enter Valid Amount')

                else:
                    x.amount-=int(amt)
                    c = customer.objects.get(id=x.id)
                    c.amount = x.amount

                    custid2 = x.id
                    c.save()
                    for y in customers:
                        if y.name==rec:
                            y.amount+=int(amt)
                            c= customer.objects.get(id=y.id)
                            c.amount=y.amount
                            tempid1 = y.name
                            custid=y.id
                            c.save()


        if custid==-1 or custid2==-1:

            return render(request,"transfer.html",{"get":tempid1,"customers":customers,"getamt":ammmt})
        else:
            c1 = customer.objects.get(id=custid)
            c2 = customer.objects.get(id=custid2)
            t = Transact(senname=c2.name, recname=c1.name, senamt=ammt, curbal=c2.amount)
            t.save()
            messages.info(request, 'Transaction is Succesful')
            messages.info(request, f'{ammt} was successfully transfered to {c1.name}')
            ammmtt = c2.amount

            tempid11 = c2.name

            ammmt=0
            custid=-1
            tempid1=""
            tempid2=""
            custid2=-1

            return render(request,"transfer.html",{"get":tempid11,"customers":customers,"getamt":ammmtt})
def transactions(request):
    t1=Transact.objects.all()
    return render(request,"transact.html",{"transact":t1})

def view(request):
    if request.method == "POST":
        getname=request.POST['get']
        getamt=request.POST['getamt']
        customers = customer.objects.all()
        return render(request, "transfer.html", {"customers": customers, "get": getname,"getamt":getamt})
    else:
        customers=customer.objects.all()
        return render(request, "customer.html",{"customers":customers})