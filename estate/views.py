from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
import datetime as dt
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'estate/home.html')