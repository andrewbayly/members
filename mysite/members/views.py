#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the members index.")



#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TeamMember

# def index(request):
#     return HttpResponse("Hello, world! You're at the polls index.")

def index(request):
    team_member_list = TeamMember.objects.order_by('id')
    template = loader.get_template('members/index.html') 

#    output = team_member_list[0].FirstName

#    output = ', '.join([q.FirstName for q in team_member_list])
    context = {
        'team_member_list': team_member_list,
    }

    return HttpResponse(template.render(context, request))

# Leave the rest of the views (detail, results, vote) unchanged
