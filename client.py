import requests
import time
import json

client_id = None
shots = []
url = "http://localhost:5000/"

def connect():
    requests.post(url + "connect")

def shoot():
    new_shot = '{"time": time.localtime(), "client_id": client_id, "shot_id": len(shots)}'.encode("utf-8")
    print(new_shot)
    shots.append(new_shot)
    requests.post(url + "shot", data=new_shot)

def report_hit(shot_id):
    new_hit = '{"time": time.localtime(), "client_id": client_id, "shot_id": shot_id}'.encode("utf-8")
    requests.post(url + "hit", data=new_hit)

print("Attempting to connect...")
client_id = connect()
print("Connection successful.")
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
