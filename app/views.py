from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.form import *
# Create your views here.
def fbv(request):
    return HttpResponse('<h1>this is function based view</h1>')
class cbv(View):
    def get(self,request):
     return HttpResponse('<h1>this is class based view</h1>')
    

def fbvhtml(request):
   return render(request,'fbvhtml.html')
class cbvhtml(View):
   def get(self,request):
      return render(request,'cbvhtml.html') 


def insert_fbv(request):
   SFO=Schoolform()
   d={'SFO':SFO}
   if request.method=='POST':
      SFTO=Schoolform(request.POST)
      if SFTO.is_valid():
         SFTO.save()
         return HttpResponse('this is feild is function')
   return render(request,'insert_fbv.html',d)     


class insert_cbv(View):
   def get(self,request):
      EFO=Schoolform()
      d={'EFO':EFO}
      return render(request,'insert_cbv.html',d)
   def post(self,request):
      SFTO=Schoolform(request.POST)
      if SFTO.is_valid():
         SFTO.save()
         return HttpResponse('this is feild is CLASS')
      

class cbv_templates(TemplateView):
   template_name='cbv_templates.html'