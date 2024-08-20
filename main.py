import requests
from datetime import datetime

USERNAME = "ivankuria"
TOKEN = "39ytvqbgiqhevni"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph2",
    "name": "Leetcode Graph",
    "unit": "Hours",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

graph_id = graph_params["id"]

pixe_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

# gets the current date
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}

response = requests.post(url=pixe_endpoint, json=pixel_params, headers=headers)
print(response.text)
