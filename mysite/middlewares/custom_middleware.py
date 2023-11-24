from mysite.settings import comingsoon
from django.shortcuts import render
from website.forms import NewsLetterForm
from django.contrib import messages


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if comingsoon:
            if request.method == 'POST':
                form = NewsLetterForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Thanks . Your message has been received.','success')
                else:
                    messages.error(request,'Please inter correct pattern .','error')
            form = NewsLetterForm()
            context = {"form":form}
            return render(request ,'website/coming_soon/index.html',context)
        # Code to be executed for each request before
        # the view (and later middleware) are called
        response = self.get_response(request)
        
        return response