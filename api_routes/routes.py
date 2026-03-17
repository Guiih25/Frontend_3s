import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"
    headers = {
        "x-api-key": "live_1ahWFm7LuMSBcNpcpwBPDDIuggfg7n2nRUSg1K3gc3zcU9XavyKMEvX9wo0pfF1h"
    }

    resposta = requests.get(url, headers=headers)

    return resposta.json()
def get_image():
    url = "https://api.thecatapi.com/v1/images/search"
    resposta = requests.get(url)
    return resposta.json()[0]

