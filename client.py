import requests

server_url = "http://localhost:5000/"
codename = "Luke"

id = None

def connect():
    player_info = str({"codename": codename})
    return requests.post(server_url + "connect", data=player_info).text

def shoot():
    pass

def get_hit():
    pass

print("Trying to connect...")
response = eval(connect())
id = response["id"]
print("Server response: " + str(response))
print("Connected.")
