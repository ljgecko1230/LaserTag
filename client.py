import requests

server_url = "http://localhost:5000/"
codename = "Luke"

def connect():
    player_info = str({"codename": codename})
    return requests.post(server_url + "connect", data=player_info).text

print("Trying to connect...")
response = eval(connect())
print("Server response: " + str(response))
print("Connected.")
