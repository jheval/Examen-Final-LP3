from django.shortcuts import render, HttpResponse
import sqlite3

# Create your views here.

layout = """
    <h2> Examen Final (LP3 - 2024) | Valdivieso Sánchez, Jheremy </h2>
    <hr/>
"""

def index(request):
    return render(request, 'index.html')

def personas(request):
    conexion = sqlite3.connect("Valdiviesopersonas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Valdivieso_persona")
    personas = []
    
    for row in cursor.fetchall():
        if len(row) >= 3:
            fecha_registro = ""
        else:
            fecha_registro = None
        personas.append({
            'id': row[0],
            'nombre': row[1],
            'apellidos': row[2],
            'sexo': row[3],
            'fecha_de_registro': fecha_registro
        })
    cursor.close()
    conexion.close()
   
    return render(request, 'personas.html', {'personas': personas})
