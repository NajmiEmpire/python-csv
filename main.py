import requests
import csv

url = "https://api.github.com/repositories"
r = requests.get(url)

print(r.json())
