from django.shortcuts import render
import requests
from .models import Link
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    data=[]
    return render(request,'result.html',{'data':data})

def scrape(request):
    if request.method=="POST":
        site=request.POST.get("site",' ')   #inputs site name
        print(site)
        page=requests.get(site)  #tells whether the request to the site is accepted or not
        print(page)
        soup=BeautifulSoup(page.text,'html.parser')
        print('Post')
        for link in soup.find_all('a'):
            link_address=link.get('href')     #get link 
            link_text=link.string             #get name of link
            Link.objects.create(address=link_address,name=link_text)
        data=Link.objects.all()
    else:
        print('Elese..')
        data=Link.objects.all()
    return render(request,'result.html',{'data':data})



def clear(request):
    Link.objects.all().delete()
    data=[]
    return render(request,'result.html',{'data':data})