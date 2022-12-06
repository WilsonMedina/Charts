import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #get the status 
    print(r.text) #get the information/response
    print(type(r.text)) #get the datatype
    categories = r.json() #transforms the response a JSON format that python can recognize
    for category in categories:
        print(category['name'])