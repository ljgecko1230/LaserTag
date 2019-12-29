import requests
import time
import json

username = ""
client_id = None
shots = []
url = "http://localhost:5000/"

def connect():
    player_data = str({"name": username}).encode("utf-8")
    return requests.post(url + "connect", data=player_data).data["id"]

def shoot():
    new_shot = str({"time": time.localtime(), "client_id": client_id, "shot_id": len(shots)}).encode("utf-8")
    print(new_shot)
    shots.append(new_shot)
    requests.post(url + "shot", data=new_shot)

def report_hit(shot_id):
    new_hit = str({"time": time.localtime(), "client_id": client_id, "shot_id": shot_id}).encode("utf-8")
    requests.post(url + "hit", data=new_hit)

print("Attempting to connect...")
client_id = connect()
print("Connection successful.")
print("Client id: " + client_id)
print()

while True:
    print("1. Shoot")
    print("2. Get hit")
    action = input("Action? ")
    print()
    if action == "1":
        shoot()
    else:
        shot_id = input("What's the shot id? ")
        report_hit(int(shot_id))
