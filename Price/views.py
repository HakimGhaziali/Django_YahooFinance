from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import yfinance as yf
import json
import requests
from .models import Data
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

    
import yfinance as yf
import json



def fcreate(request):
    
    msft = yf.Ticker("MSFT")
    hist = msft.history(period = "1mo", interval = "1d")
    hist=hist.reset_index()
    hist = hist.reset_index()

    x= hist['index'].values
    y=hist['Close'].values
    n=0
    for i in y:
        Data.objects.create(id= n , price= i)
        n = n+1
    
    n=0

    for i in x:
        obj = Data.objects.get(pk=n)
        obj.date = i
        obj.save()
        n=n+1

    return render(request , 'home.html')

        