from django.shortcuts import render
from django.http import HttpResponse
from website.forms import  ContactForm,NewsLetterForm
from django.contrib import messages
from website.models import Information,My_Skill,Skill,UserImage
from django.shortcuts import render,get_object_or_404,redirect

def index_view(request):
    informations = Information.objects.all().first()
    context = {'informations':informations}
    return render(request ,'website/index.html',context)

def about_view(request):
    informations = Information.objects.all().first()
    img = UserImage.objects.all().first()
    context = {'informations':informations,'img':img}
    return render(request ,'website/about.html',context)

def resume_view(request):
    return render(request ,'website/Resume.html')

def skill_view(request):
    info  = Skill.objects.all().first()
    skills = My_Skill.objects.all()
    context = {'skills':skills,'info':info}
    return render(request ,'website/skill.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks . Your message has been received.')
        else:
            messages.error(request,'Please inter correct pattern .','error')
    form = ContactForm()
    informations = Information.objects.all().first()
    context = {'informations':informations,'form':form}
    return render(request,'website/contact.html',context)

