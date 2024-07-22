from django.shortcuts import render,HttpResponse

# Create your views here.


layout = """
    <h2> Examen Final (LP3 - 2024) | Valdivieso Sánchez, Jheremy </h2>
    <hr/>
    
"""



def index(request):
    mensaje="""
    <ul>
        <li>
            <a href="/personas"> Opción Personas</a>
        </li>
    </ul>    
    
    <hr/>
    
        (Página de inicio)
    """
    return HttpResponse(layout+mensaje)



def personas(request):
    mensaje ="""
        <h1>Pagina de personas</h1>
    """
    return HttpResponse(layout+mensaje)

