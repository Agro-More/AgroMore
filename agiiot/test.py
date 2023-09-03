# import os

# curr_loc = os.path.dirname(os.path.realpath(__file__))
# print(curr_loc)



import requests

url = "http://localhost:5000/recommend"
data = {
    "K": 200,
    "N": 20,
    "P": 125,
    "temperature": 20.879744,
    "humidity": 82.002744,
    "ph": 5.5,
    "rainfall": 100.935536
}
postresponse = requests.post(url, json=data)
print("postresponse: ", postresponse.json())


# Change the URL to your API endpoint
url = "http://localhost:5000/crops"  
params = {
    "name": "maize",  
    }

getresponse = requests.get(url, params=params)
print("getresponse: ", getresponse.json())

# http://127.0.0.1:5000/crops/?name=cotton
# http://localhost:5000/crops/?name=cotton

# http://127.0.0.1:8000/recommend-data/?api_key=286ae6c3-bb25-4f6f-8cc4-c06e6004cbe2
