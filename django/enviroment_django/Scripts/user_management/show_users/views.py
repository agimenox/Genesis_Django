from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def show_all_users(request):
    
    template_show_all_users = open('C:/Repo_GitHub/Genesis_Django/django/enviroment_django/Scripts/user_management/show_users/templates/show_users.html')   

    template_doc = Template(template_show_all_users.read())

    template_show_all_users.close()

    ctx = Context()

    final_view = template_doc.render(ctx)

    return HttpResponse(final_view)