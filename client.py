import requests

server_url = "http://localhost:5000/"
codename = "Luke"

id = None

def connect():
    player_data = str({"codename": codename})
    return eval(requests.post(server_url + "connect", data=player_data).text)

def send_attack():
    pass

def recieve_attack():
    pass

def get_player_stats():
    return eval(requests.get(server_url + "stats/" + str(id)).text)

print()
print("Trying to connect...")

response = connect()
id = response["id"]

print("Server response: " + str(response))
print("Connected.")

print()
print("Updating player information...")

response = get_player_stats()

print("Server response: " + str(response))

while True:
    pass
