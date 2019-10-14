# Virtual Environment
"""
To create virtual environment: <python> - m venv name_of_environment
To activate virtual environment:
    Windows: name_of_environment/scripts/activate
    Unix:    source name_of_environment/bin/activate
"""

import requests
from pprint import pprint

# # getting information from rockets and assigning to variables
# response = requests.get("https://api.spacexdata.com/v3/rockets")
# data = response.json()  # JS Object Notation (standard data schematic/non performant)

# for entry in data:
#     print(entry['rocket_name'], "\n") # print .keys() of all after checking data type()

# Challenge
# Find how many characters in API 

api_url = "https://rickandmortyapi.com/api/"

character_response = requests.get(api_url + "character")

try:
    data = character_response.json()
except Exception:
    data = None

print(data.keys())
# print(type(data['results'][-1]))
# print(len(data['results'])) <-- does not show everything 20 vs 493
choices = data['info']['count']

choice = input(f"Pick a no. between 1 and { choices } >")

chosen = requests.get(api_url + "character/" + choice)
chosen_one = chosen.json()
print(chosen_one["name"])

print(chosen.headers)

