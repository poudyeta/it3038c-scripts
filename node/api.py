import json 
import requests 
 
 
r = requests.get('http://localhost:3000/') 
data=r.json() 
for widget in data:
    print (f"{widget.get('name')} is {widget.get('color')}")