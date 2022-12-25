from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_all_users(request):

    table = """
    <html>
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
                <th>Usuario</th> <!--Cabezera o titulo de la columna-->
                <th>Permiso</th>
            </tr> <!--Table Route o una fila dentro de la tabla-->
        </thead>
        <tbody>
            <tr>
                <td>Andres</td> <!--se utiliza para definir elementos estandares dentro de la tabla-->
                <td>Admin</td>
            </tr>
            <tr>
                <td>Logan</td> <!--se utiliza para definir elementos estandares dentro de la tabla-->
                <td>Super User</td>
            </tr>
            <tr>
                <td>Chompi</td> <!--se utiliza para definir elementos estandares dentro de la tabla-->
                <td>User</td>
            </tr>
        </tbody>
</html>
    
    
    
    
    """
    return HttpResponse(table)