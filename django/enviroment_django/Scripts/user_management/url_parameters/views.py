from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.

def half_number(request, name, number):
    new_number = number / 2
    template_doc_half_number = open("C:/Repo_GitHub/Genesis_Django/django/enviroment_django/Scripts/user_management/url_parameters/templates/half_number.html")
    template_doc = Template(template_doc_half_number.read())
    template_doc_half_number.close()
    ctx = Context({'person_name':name,'half_number':new_number})
    final_view = template_doc.render(ctx)
    
    return HttpResponse (final_view)
