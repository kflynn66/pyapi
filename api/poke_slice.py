# Get poke slice for image
import requests

poke_api = "https://pokeapi.co/api/v2/pokemon/bulbasaur/"
json2python = requests.get(poke_api).json()

print(json2python)

def api_slice(json2python):
    global poke_pic
    poke_pic = json2python["sprites"]["front_default"]
    return poke_pic

print(api_slice(json2python))
print(poke_pic)
# api_slice(https://pokeapi.co/api/v2/pokemon/bulbasaur/) # this is a temporary link

