from django.shortcuts import render,redirect
from .models import Nutri
from .forms import NutriForm, BMIForm, WeightForm
from django.contrib import messages

# Create your views here.
#GQDnoEPUNnfMC0qQ8CyVCQ==PrzpsqB45adMvegv


def home(request):
    import json
    import requests
    if request.method=='POST':
        query = request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request= requests.get(api_url + query, headers={'X-Api-Key':'GQDnoEPUNnfMC0qQ8CyVCQ==PrzpsqB45adMvegv'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api= "OOPS! There was an error!"
            print(e)
        context={
            'api':api
        }
        return render(request,'hm.html',context)
    else:
        return render(request,'hm.html',{'query':'Enter the Valid Query'})




def reg(request):
    users = Nutri.objects.all()
    if request.method == 'POST':
        form=NutriForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('Name')
            messages.success(request,f'{name} has been inserted')
            age=form.cleaned_data['Age']
            gen=form.cleaned_data['Gender']
            h=form.cleaned_data['Height']
            w=form.cleaned_data['Weight']
            bmass_r=bmr(age,gen,h,w)
            wg_10=round((bmass_r+(bmass_r*0.1)),2)
            wg_20=round((bmass_r+(bmass_r*0.2)),2)
            wg_35=round((bmass_r+(bmass_r*0.35)),2)
            wl_10=round((bmass_r-(bmass_r*0.1)),2)
            wl_20=round((bmass_r-(bmass_r*0.2)),2)
            wl_35=round((bmass_r-(bmass_r*0.35)),2)
            context={
                'users':users,
                'bmass_r':bmass_r,
                'wg_10':wg_10,
                'wg_20':wg_20,
                'wg_35':wg_35,
                'wl_10':wl_10,
                'wl_20':wl_20,
                'wl_35':wl_35
                
            }
            return render(request,'bmr.html',context)     
    else:
        form=NutriForm()
    context={
        'users':users,
        'form':form
    }
    return render(request,'profile.html',context)


def bmr(age,gen,h,w):
    bmr=0
    if gen=='Male':
        bmr=(9.99*w)+(6.25*h)-(4.92*age)+5
    elif gen=='Female':
        bmr=(9.99*w)+(6.25*h)-(4.92*age)-151
    return round(bmr,2)




def level(gen,bmr):
    if gen=="Male":
        if bmr>=2 and bmr<=5:
            return "Essential Fat"
        elif bmr>=6 and bmr<=13:
            return "Athletes"
        elif bmr>=14 and bmr<=17:
            return "Fitness"
        elif bmr>=18 and bmr<=24:
            return "Average/Normal"
        elif bmr>=25 and bmr<=29:
            return "Overweight"
        else:
            return "Obese"
    elif gen=="Female":
        if bmr>=10 and bmr<=13:
            return "Essential Fat"
        elif bmr>=14 and bmr<=20:
            return "Athletes"
        elif bmr>=21 and bmr<=24:
            return "Fitness"
        elif bmr>=25 and bmr<=31:
            return "Average/Normal"
        elif bmr>=32 and bmr<=39:
            return "Overweight"
        else:
            return "Obese"
    

def bmi(request):
    users=Nutri.objects.all()
    if request.method == 'POST':
        form=NutriForm(request.POST)
        if form.is_valid():
            form.save()
            gen=form.cleaned_data['Gender']
            h=form.cleaned_data['Height']
            w=form.cleaned_data['Weight']
            body_i=cal_bmi(h,w)
            lvl=level(gen,body_i)
            context={
                'body_i':body_i,
                'lvl':lvl
            }
            messages.success(request,f'BMI is {body_i}')
            return render(request,'report.html',context)
    else:
        form=NutriForm()
    context={
        'form':form,
        'users':users
    }
    return render(request,'bmi.html',context)


def cal_bmi(h,w):
    hm=h/100
    bmi=w/(hm**2)
    return round(bmi,2)



def report(request):
    return render(request,'report.html')