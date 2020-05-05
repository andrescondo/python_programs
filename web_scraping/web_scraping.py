#Librerias externas / dependencia
import requests
from bs4 import BeautifulSoup
import urllib


def run():
    for i in range(1,6):
        response = requests.get('https://xkcd.com/{}'.format(i)) #conseguir informacion get de sitio/basededatos
        soup = BeautifulSoup(response.content, 'html.parser') # soup recibe dos parametos(contenido , y que tipo de cont)
        image_container = soup.find(id='comic') #find= encontrar el nodo (nodo)

        image_url = image_container.find('img')['src']# encontrar la etiqueta (img) y acceder a su atributo[src]
        image_name = image_url.split('/')[-1] #encontrar el nombre buscando el ultimo elemento del enlace
        print('Descargando la imagen {}'.format(image_name))
        urllib.request.urlretrieve('https:{}'.format(image_url), image_name)#url de donde se encuentra la imagen




if __name__ == '__main__':
    run()


