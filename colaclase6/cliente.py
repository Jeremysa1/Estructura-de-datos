import requests
import random

url = 'https://humble-guide-7v7xjpwqxp9hjww-8000.app.github.dev'

names = ["Jeremy", "jesus", "andres", "kerly", "melissa"]
last_names = ["sanchez", "gonzales", "giron", "cordoba", "morales"]
items = ["Frutas", "zapatos", "ropa deportiva", "detergentes", "utiles escolares"]

def generate_element():
    first_name = random.choice(names)
    last_name = random.choice(last_names)
    products = [random.choice(items) for _ in range(2)]
    return {
        "name": f"{first_name} {last_name}",
        "products": products
    }

for _ in range(5):
    element_to_enqueue = generate_element()
    response = requests.post(f'{url}/encolar', json=element_to_enqueue)
    
    if response.status_code == 40:
        data = response.json()
        print(f"Element enqueued successfully: {data}")
    else:
        print(f'Error in POST to /encolar: {response.status_code}')

