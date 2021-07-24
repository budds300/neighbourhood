from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
import datetime as dt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.
def home(request):
    return render(request,'estate/home.html')