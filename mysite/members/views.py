from django.http import HttpResponse
from django.template import loader
from .models import TeamMember
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from .forms import MemberForm

from django.http import HttpResponseRedirect
from django.shortcuts import render

import json

def index(request):
    
    if request.method == 'GET' :
    
        team_member_list = TeamMember.objects.order_by('id')

        template = loader.get_template('members/index.html') 

        context = {
            'team_member_list': team_member_list,
        }

        return HttpResponse(template.render(context, request))
        

def save(request):
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
    
        # Note: we can get here from Add or Edit screen when we hit Save button.
    
        # create a form instance and populate it with data from the request:
        form = MemberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            the_id = form.cleaned_data["Id"]
            
            t = TeamMember()
            
            if the_id != -1 : 
                t = TeamMember.objects.filter(id=form.cleaned_data["Id"])[0]

            t.FirstName = form.cleaned_data["FirstName"]
            t.LastName = form.cleaned_data["LastName"]
            t.Phone = form.cleaned_data["Phone"]
            t.Email = form.cleaned_data["Email"]
            t.Admin = form.cleaned_data["Admin"]
    
            t.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect("/")

    elif request.method == "GET":
    
        form = MemberForm(initial={
            'Id': -1, 
            'Admin':False 
        })
        
        return render(request, "members/edit.html", {"form": form})
        
        
def edit(request, id):

    if request.method == 'GET' :

        team_member = TeamMember.objects.get(id=id)
    
        context = {
            'team_member' : team_member
        } 

        form = MemberForm(initial={
            'Id': id, 
            'FirstName': team_member.FirstName, 
            'LastName': team_member.LastName, 
            'Email': team_member.Email, 
            'Phone': team_member.Phone, 
            'Admin': team_member.Admin
        })

        return render(request, "members/edit.html", {"form": form, 'team_member' : team_member})


@csrf_exempt
def delete(request, id):
    
    team_member = TeamMember.objects.get(id=id)
    team_member.delete()
    
    return HttpResponse()

        
        