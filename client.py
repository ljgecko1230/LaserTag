import requests
import time
import sys

server_url = "http://localhost:5000/"
codename = "Luke"
id = None
current_stats = None

def connect():
    print("Trying to connect...")

    player_data = str({"codename": codename})
    return_data = eval(requests.post(server_url + "connect", data=player_data).text)

    print("Connected.")

    return return_data

def send_attack():
    print("Sending shot...")

    shot_data = str({"time": time.time(), "player": id})
    requests.post(server_url + "shot", data=shot_data)

    print("Shot sent.")

def recieve_attack():
    pass

def get_player_stats():
    print("Updating player information...")

    return_data = eval(requests.get(server_url + "stats/" + str(id)).text)

    print("Done.")

    return return_data

print()
while True:
    print()
    print("SERVER URL: " + server_url)
    print("CODENAME: " + codename)
    if id != None:
        print("CLIENT ID: " + str(id))
        print("HEALTH: " + str(current_stats["health"]))
        print("SCORE: " + str(current_stats["score"]))
        print("1. Shoot")
        print("2. Take hit")
        print("3. Disconnect")
        choice = input("Choice: ")

        if choice == "1":
            send_attack()
            get_player_stats()

        elif choice == "2":
            print("ouch. choice not available at this time.")

        elif choice == "3":
            print("Disconnecting... choice not available at this time.")

        else:
            print("That is not a valid choice. Please select again.")

    else:
        print("1. Connect to server")
        print("2. Configure settings")
        choice = input("Choice: ")

        if choice == "1":
            player_data = connect()
            id = player_data["id"]
            current_stats = get_player_stats()

        elif choice == "2":
            new_server_url = input("New server URL (blank to leave unchanged): ")
            if new_server_url:
                server_url = new_server_url

            new_codename = input("New codename (black to leave unchanged): ")
            if new_codename:
                codename = new_codename

        else:
            print("That is not a valid choice. Please select again.")

while True:
    pass
