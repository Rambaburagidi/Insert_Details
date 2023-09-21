from django.shortcuts import render

from .models import insert
# Create your views here.
def home(request):
    if request.method=="GET":
        k=insert.objects.all()
        return render(request,"e.html",{'k':k})
