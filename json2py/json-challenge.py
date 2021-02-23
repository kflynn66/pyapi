
import json

def jsonify():
    with open("challenge.json", "r") as jsonfirst:
        testjson = jsonfirst.read()
    realjson = json.loads(testjson)
    return realjson

def printdata(sample):
    for x in sample:
        print(f"Name: {x['name']}")
        print(f"Email: {x['email']}")
        print(f"Phone: {x['phone']}")
        print(f"Address: {x['address']}")
        for y in sample:
         print(f"Friends: {x['friends'][y]['name']}")


def main(): 
   printdata(jsonify())

if __name__ == "__main__":
    main()

