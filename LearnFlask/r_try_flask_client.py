import requests

BASE = "http://127.0.0.1:5000/"
headers = {"Content-Type": "application/json"}
data = [
    {"name":"python", "views": 40,"likes":10},
    {"name":"JavaScript", "views": 41,"likes":11},
    {"name":"Node.js", "views": 42,"likes":12}
]

""" for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i], headers=headers)
    print(response)
    print(response.json()) """

input()

""" response = requests.delete(BASE + "video/0")
print(response)
#print(response.json()) """

""" response = requests.get(BASE + "video/12")
print(response)
print(response.json()) """

response = requests.patch(BASE + "video/2", json={"views" : 99, "likes" : 999}, headers=headers)
print(response)
print(response.json())