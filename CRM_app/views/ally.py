from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

class Ally(View):
    def get(self, request):
            return render(request, 'allies/single-page-ally.html')
        
            
    
    