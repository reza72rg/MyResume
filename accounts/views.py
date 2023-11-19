from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

          
# Create your views here.

class UserLoginView(View):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    
 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        global next
        next = request.GET.get('next')
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self, request):
       
        form = self.form_class(request=request,data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)       
                if next:
                    messages.success(request,'you are login successfuly','success')
                    return redirect(next)
                messages.success(request,'you are login successfuly','success')
                return redirect('/')
                # Redirect to a success page.
            
        else:
            messages.error(request,'username or password is wrong','danger')
      
        return render(request,self.template_name,{'form':form})   
         

class UserLogOut(LoginRequiredMixin, View):
    login_url = 'accounts/login.html'  
    def get(self,request):
        logout(request)
        messages.success(request, 'you are logout successfuly.')
        return redirect('/')
        
   

class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'accounts/singup.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password1'])
            user = authenticate(request, username=cd['username'], password=cd['password1'])
            user.save()
            messages.success(request,'Thanks . Your registration was successfuly plase log in.','success')
            if user is not None:
                login(request, user)
                return redirect("/")
        else:
            messages.error(request,'Please input the correct password','danger')
            
        return render(request,self.template_name,{'form':form})

class UserPasswordResetView(auth_views.PasswordResetView):
	template_name = 'accounts/changepassword.html'
	success_url = reverse_lazy('accounts:password_reset_done')
	email_template_name = 'accounts/password_reset_email.html'
 
class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name = 'accounts/password_reset_done.html'
 
class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'accounts/password_reset_confirm.html'
	success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name = 'accounts/password_reset_complete.html'


