#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/pyapi/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds


# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    adopdate = input("Enter a date to lookup [YYYY-MM-DD] " )

    ## make a call to NASAAPI with our key
    reqapi = (f"{NASAAPI}{nasacreds}&date={adopdate}&thumbs=true")
    apodresp = requests.get(reqapi)

    ## strip off json
    apod = apodresp.json()
    
    if "video" in apod['media_type']: 
       print(apod['thumbnail_url'])
    else: 
        print(apod['url'])


if __name__ == "__main__":
    main()

