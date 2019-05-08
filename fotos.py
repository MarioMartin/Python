import json
import requests
import webbrowser

def request (URL, APi_KEY):

    URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol=1900&camera=NAVCAM"
    KEY = "DEMO_KEY"

    params = {
        "api_key": KEY
    }

    respuesta = requests.get(URL, params=params)

    if respuesta.status_code == 200:
        results = respuesta.json()
        fotos = results["photos"]
        return fotos 
    else:
        print("No se pudo obtener la imagen.")
        return 0


fotos = request("ddd","ddd")

pagina = open('index.html','w')


mensaje = """<html><head></head><body><ul>"""

lista=""
for value in fotos:
    url = value['img_src']
    lista = lista + "<li><img src='"+url+"'></li>"
    
    print(url)

mensaje =  mensaje + lista
mensaje =  mensaje + "</ul></body></html>"

pagina.write(mensaje)
pagina.close()

nombreArchivo = "index.html"
webbrowser.open_new_tab(nombreArchivo)
           
##

    
   

