#!/usr/bin/python3

# pip install requests 
import requests

while True:
    search_string = input('Country: ')
    response = requests.get('https://restcountries.eu/rest/v2/name/' + search_string)
    print(response.text)
