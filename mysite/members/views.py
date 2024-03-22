from django.http import HttpResponse
from django.template import loader
from .models import TeamMember
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def index(request):
    print(request.method)

    if request.method == 'GET' :

        team_member_list = TeamMember.objects.order_by('id')

        template = loader.get_template('members/index.html') 

        context = {
            'team_member_list': team_member_list,
        }
        
    elif request.method == 'PUT' :    
        body = json.loads(request.body)
    
        t = TeamMember()
                
        t.FirstName = body['FirstName'] 
        t.LastName = body['LastName'] 
        t.Phone = body['Phone'] 
        t.Email = body['Email']
        t.Admin = False #TODO! 
        t.save()
                
        return HttpResponse()

    return HttpResponse(template.render(context, request))

def add(request):

    print("Add...") 

    template = loader.get_template('members/edit.html')
  
    context = {
        'team_member' : None
    } 

    return HttpResponse(template.render(context, request))


@csrf_exempt
def edit(request, id):
    print(request.method)
    
    if request.method == 'POST' :
        body = json.loads(request.body)
    
        t = TeamMember.objects.filter(id=int(body['id']))[0]
                
        t.FirstName = body['FirstName'] 
        t.LastName = body['LastName'] 
        t.Phone = body['Phone'] 
        t.Email = body['Email'] 
        t.save()
                
        return HttpResponse()
        
    elif request.method == 'GET' :

        team_member = TeamMember.objects.get(id=id)
    
        template = loader.get_template('members/edit.html')
    
        context = {
            'team_member' : team_member
        } 

        return HttpResponse(template.render(context, request))

    elif request.method == 'DELETE' :

        team_member = TeamMember.objects.get(id=id)
        team_member.delete()
    
        return HttpResponse()