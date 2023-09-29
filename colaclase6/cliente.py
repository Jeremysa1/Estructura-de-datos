import requests

url = 'https://scaling-lamp-g4q76465w5rvcppx4-8000.app.github.dev/'

# ejemplo request en GET
r = requests.get(url)
print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'nombre': 'Jeremy', 'productos': ['kiwi', ],"CC":78945})
r = requests.post(url + 'encolar', json={'nombre': 'Andres', 'productos': ['Manzana'],"CC":654321})
r = requests.post(url + 'encolar', json={'nombre': 'Jesus', 'productos': ['Carambolo'],"CC":55789})
r = requests.post(url + 'encolar', json={'nombre': 'Kerly', 'productos': ['Longaniza'],"CC":96321})
r = requests.post(url + 'encolar', json={'nombre': 'Melissa', 'productos': ['tomate'],"CC":14789})
print(r.text)