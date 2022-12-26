from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime

# Create your views here.
class Person():
    def __init__(self,name,username,password) -> None:
        self.name = name
        self.username = username
        self.password = password
        self.permission = 'Guest'
        self.creationdate = datetime.datetime.now()
        pass
    

def register_new_user(request, name, username, password):
    person = Person(name,username,password)
    template_doc_front = open("C:/Repo_GitHub/Genesis_Django/django/enviroment_django/Scripts/user_management/url_parameters/templates/half_number.html")
    template_doc = Template(template_doc_front.read())
    template_doc_front.close()
    ctx = Context({'person_name':person.name,'username':person.username,'creation_date':person.creationdate})
    final_view = template_doc.render(ctx)
    
    return HttpResponse (final_view)
