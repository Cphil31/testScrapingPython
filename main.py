import requests
from bs4 import BeautifulSoup

url ='https://kalendrier.ouest-france.fr/liste-pays-monde.html'

response = requests.get(url)
# récuperer le code html de la page
#on vas le passer dans la fonction Beautifulsoup
if response.ok:
    #print(response.text)
    #ne pas oublier de le parser en 2nd argument
    soup = BeautifulSoup(response.text,"html.parser")

    #je recupère un tableau
    allPays = soup.findAll('td')
    #je crée le tableau vide des pays
    links = []
    #je parcours mon tableau et je l'affiche
    #je parcours mon tableau
    for pays in allPays:

        #je recupere le a href de chaque pays
        a = pays.find("a")
        href = a.get('href')
        print("https://kalendrier.ouest-france.fr/" + href)
















