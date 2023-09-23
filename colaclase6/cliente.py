import requests

url = 'https://miniature-goggles-v6vqw6wg75g53wprg-8000.app.github.dev/encolar'

# ejemplo request en POST
r = requests.post(url, json={'nombre': 'Diego', 'productos': ['leche', 'chocolate']})
print(r.text)