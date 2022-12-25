from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def half_number(request, name, number):
    new_number = number / 2
    doc_with_response = """
    <head>
        <title>Show Users</title> <!--Titulo de pagina WEB-->
        <style>
            table, th, td {
                border: 1px solid black;       <!--para dibujar el cuadro negro--> 
            }
        </style>
    </head>
    <body>
        <table style="width: 500px;"> <!--aumenta el tamaño de los espacios dentro de las celdas-->
            <thead>
                <tr>
                    <th>%s!! Your Half Number is </th> <!--Cabezera o titulo de la columna-->
                    <th>%s</th>
                </tr> <!--Table Route o una fila dentro de la tabla-->
            </thead>
    </tbody>
    
                        """ %(name, new_number)
    return HttpResponse (doc_with_response)
