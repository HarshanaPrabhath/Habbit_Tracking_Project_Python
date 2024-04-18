import requests
from datetime import datetime
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
GRAPH_ID = "graph01"

graph_configuration = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_configuration,headers=headers)
# print(graph_response.text)


# ....................post graph.........................

post_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today = today.strftime("%Y%m%d")

post_graph_config = {
    "date": today,
    "quantity": "50",
}

post_graph_response = requests.post(url=post_graph, json=post_graph_config, headers=headers)
print(post_graph_response.text)
