from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader
from django.shortcuts import render

# Create your views here.
class Person():
    def __init__(self,name,username,password) -> None:
        
        self.name = name
        self.username = username
        self.password = password
        self.creationdate = datetime.datetime.now()
        self.groups = ['guest']
        pass
    

def register_new_user(request, name, username, password):

    person = Person(name,username,password)
    return render(request, "user_registration.html",{'person_name':person.name,'username':person.username,'creation_date':person.creationdate,'groups':person.groups})
