import requests

# ...................create account ...................
pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "ughpk20030630"
USERNAME = "harshana2003"

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

# ....................create graph.........................

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph01",
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_response = requests.post(url=graph_endpoint, json=graph_configuration,headers=headers)
print(graph_response.text)
