from django.shortcuts import render
from .forms import ContactForm, NewsLetterForm
from django.contrib import messages
from .models import MySkill, Skill, UserImage, ProfessionalExperience, Education


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    img = UserImage.objects.all().first()
    context = {'img': img}
    return render(request, 'website/about.html', context)


def resume_view(request):
    profess = ProfessionalExperience.objects.filter(status=1)
    educate = Education.objects.filter(status=1)
    context = {'profess':profess,'educate':educate}
    return render(request ,'website/Resume.html',context)


def skill_view(request):
    info = Skill.objects.all().first()
    skills = MySkill.objects.all()
    context = {'skills': skills, 'info': info}
    return render(request, 'website/skill.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks . Your message has been received.', 'success')
        else:
            messages.error(request, 'Please inter correct pattern .', 'error')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html', context)


def coming_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks . Your message has been received.', 'success')
        else:
            messages.error(request, 'Please inter correct pattern .', 'error')
    form = NewsLetterForm()
    context = {"form": form}
    return render(request, 'website/coming_soon/index.html',context)
