from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm,CutLinkForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Author

import pyshorteners

list_of_urls = []

class BaseInformation(ListView):
    model = User
    template_name = 'Link/base.html'

@login_required
def cut_method(request):
    short = ""
    if request.method == "POST":
        form = CutLinkForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['URL']
            short = pyshorteners.Shortener().tinyurl.short(url)
            links = Author.objects.filter(author=request.user).get().links
            Author.objects.filter(author=request.user).update(links = links + short + ';')

    else:
        form = CutLinkForm()
    return render(request,'Link/cut_the_link.html',{'form':form,"short":short})
@login_required
def show_links(request):
    name = Author.objects.filter(author=request.user)
    urls = name.get().links
    return  render(request,'Link/profile.html',{"urls":urls})

class UserRegister(SuccessMessageMixin,CreateView):
    form_class = UserRegisterForm
    template_name = 'Link/register.html'
    success_url = reverse_lazy('base-home')
    success_message = f'Your account has been created! You are now able to log in'
