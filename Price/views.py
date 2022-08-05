from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import yfinance as yf
import json
import requests
from .models import Data , Ticker
from django.views import generic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
import yfinance as yf
import json
from django.views import generic
from .forms import DataCreateForm
from django.urls import reverse_lazy





class ChartCreate(generic.CreateView):

    form_class = DataCreateForm
#    fields= '__all__'
    template_name = 'chartcreate.html'
    success_url = reverse_lazy('display')
    


def fcreate(request):
    'this function import data from Yfinance'

    entries= Data.objects.all()
    entries.delete()
    
    obj = Ticker.objects.last()
    
    msft = yf.Ticker(obj.ticker)
    hist = msft.history(period = "1mo", interval = "1d")
    hist=hist.reset_index()
    hist = hist.reset_index()
    x= hist[['index' , 'Close']].values

    for i , ii in x:

        valu = Data.objects.create(ticker = obj.ticker , price = ii , date = i )

    return render(request , 'home.html' , { 'Data': Data.objects.all()  })

        