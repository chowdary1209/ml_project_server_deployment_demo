import requests

url = "http://localhost:5000/results"

r = requests.post(url, json={"Experience":3})

print(round(float(r.text),2))