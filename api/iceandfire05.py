#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/?name="

def main():
        ## Ask user for input
        got_charToLookup = input("Enter a Character Name! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        # pprint.pprint(got_dj)
        got_house = got_dj[0]['allegiances'][0]
        got_books = got_dj[0]['books']

        print(got_books)

        houseresp = requests.get(got_house)
        got_house = houseresp.json()
        print(f"Overlord: {got_house['name']}")

if __name__ == "__main__":
        main()

