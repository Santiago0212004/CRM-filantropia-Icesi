from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,logout, authenticate
from CRM_app.models import Investigation_Project, Allie, AllieProject
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

class InvestigationsProjectsAlly(View):
    
   
    def get(self, request, allie__id):
        query = request.GET.get('q', '').strip()
        if query != "":
            investigation_projects = investigation_projects.filter(Q(name__istartswith=query))
        
        try:
            allies_project= Allie.objects.get(id=allie__id)
        except Allie.DoesNotExist:
            allies_project=None
            
        try:
            projects= AllieProject.objects.filter(allie=allies_project)
            investigation_projects=[]
            for p in projects:
                investigation_projects.append(p.investigation_project)
        except AllieProject.DoesNotExist:
            investigation_projects=[]
        
        
        return render(request,'allies/single-page-ally-investigation.html',{'investigation_projects':investigation_projects})