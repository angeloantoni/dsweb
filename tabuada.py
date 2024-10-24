import sys   

from django.conf import settings    

from django.urls import path    

from django.http import HttpResponse    

settings.configure(DEBUG=True, SECRET_KEY='segredo',  

ROOT_URLCONF=__name__)    

 
 

def tabuada(request,valor):   

    s = '<style>table{border: 2px solid orange;background-color:grey;border-spacing: 0;}th,td{border: 2px solid orange;vertical-align: bottom;padding: 5px;}</style>' 

    s += '<table><thead><tr><th>Número</th><th>Multiplicado</th><th>Resultado</th></tr></thead>' 

    for i in range(1,11): 

        s += '<tbody><tr><td>' + str(valor) + '</td><td>' + str(i) + '</td><td>' + str(i * valor) + '</td></tr></tbody>' 

    s += '</table>' 

    return HttpResponse(s)  

def tabuada_view(request):
    base_url = "http://127.0.0.1:8080/tabuada/"
    links = ''.join([f'<a href="{base_url}{i}"> Tabuada do {i}</a> <br>' for i in range(1, 11)]) 
    return links

def hello(request):  
    links = tabuada_view()
    #return HttpResponse('<h1>Olá Mundo</h1> <br> <a href="http://127.0.0.1:8080/tabuada/1"> Tabuada do 1</a> <br> <a href="http://127.0.0.1:8080/tabuada/2"> Tabuada do 2</a> <br> <a href="http://127.0.0.1:8080/tabuada/3"> Tabuada do 3</a> <br> <a href="http://127.0.0.1:8080/tabuada/4"> Tabuada do 4</a> <br> <a href="http://127.0.0.1:8080/tabuada/5"> Tabuada do 5</a> <br> <a href="http://127.0.0.1:8080/tabuada/6"> Tabuada do 6</a> <br> <a href="http://127.0.0.1:8080/tabuada/7"> Tabuada do 7</a> <br> <a href="http://127.0.0.1:8080/tabuada/8"> Tabuada do 8</a> <br> <a href="http://127.0.0.1:8080/tabuada/9"> Tabuada do 9</a> <br> <a href="http://127.0.0.1:8080/tabuada/10"> Tabuada do 10</a>') 
    return HttpResponse(f'<h1>Olá Mundo</h1> <br> {tabuada_view(request)}')

def oi(request,nome): 
    return HttpResponse('Olá, ' + nome) 

 

urlpatterns = [path("tabuada/<int:valor>",tabuada),path('ola/<str:nome>',oi), path('', hello)]    

 
 

if __name__ == '__main__':    

    from django.core.management import execute_from_command_line    

    execute_from_command_line(sys.argv)    