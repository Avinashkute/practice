import datetime
from .models import crop_loan
from .forms import cropForm,signupForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def loan(request):
    time=datetime.datetime.now()

    h=int(time.strftime('%H'))
    msg = 'Hello Guest !!!! Very Very Good '
    if h<12:
        msg+='Morning'
    elif h<16:
        msg+='Afternoon'
    elif h<21:
        msg+='Evening'
    else:
        msg+='Night'
    my_dict = {'insert_time': time, 'Name': 'Avinash','msg':msg}

    return render(request,'loan/loan.html',context=my_dict)
@login_required()
def show_crop(r):
    crop_list=crop_loan.objects.get(id=1)
    print(type(crop_list))
    my_dict={'crop_list':crop_list}
    return render(r,'loan/loan.html',context=my_dict)

def crop_form(r):
    form=cropForm()
    if r.method=='POST':
        form=cropForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            return HttpResponse('<h1>Thank you for visiting</h1>')
    return render(r,'loan/form.html',{'form':form})

def reg_form(r):
    form=signupForm()
    print('ok')
    if r.method=='POST':
        form=signupForm(r.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password).save()
            print(user)

        return render(r,'accounts/')
    return render(r,'signup.html',{'form':form})