from flask import Flask, render_template, request, Response

app = Flask(__name__)

global players
players = {}
global next_available_id
next_available_id = 0

class Player:
    def __init__(self, id, codename):
        self.id = id
        self.codename = codename
        self.health = 100
        self.score = 0
        self.shots = []
        self.hits_taken = []
        self.hits_given = []

class Weapon:
    def __init__(self, type, magazine_capacity, max_ammo_storage, power,\
                 fire_rate, reload_speed):
        self.type = type
        self.magazine_capacity = magazine_capacity
        self.max_ammo_storage = max_ammo_storage
        self.reload_speed = reload_speed
        self.fire_rate = fire_rate
        self.power = power

class Event:
    def __init__(self, time, player):
        self.id = len(players[player].shots)
        self.time = time
        self.player = players[player]

class Shot(Event):
    pass

class Hit(Event):
    pass

@app.route("/", methods=["GET"])
def homepage():
    print()
    print("Loading homepage...")
    player_list = [" - " + str(id) + ": " + str(player.codename)\
                           for id, player in players.items()]

    return render_template("home.html", player_list=player_list)

@app.route("/connect", methods=["POST"])
def connect():
    global players
    global next_available_id

    print()
    print("Client attempting to connect...")

    player_data = eval(request.data)

    print("Player info: " + str(player_data))

    new_player = Player(next_available_id, player_data["codename"])
    players[new_player.id] = new_player
    next_available_id += 1

    print("Player created.")

    return_data = str({"id": new_player.id})
    response = Response(return_data, status=200, mimetype="text/plain")

    print("Returning response (" + str(response) + ").")

    return response

@app.route("/shot", methods=["POST"])
def recieve_attack_data():
    print()
    print("Client sending shot...")

    attack_data = eval(request.data)
    new_shot = Shot(attack_data["time"], attack_data["player"])

    print("Shot created.")

    new_shot.player.shots.append(new_shot)

    response = Response(status=200)

    print("Returning response (" + str(response) + ").")

    return response

@app.route("/hit", methods=["POST"])
def recieve_hit_data():
    print()
    print("Client sending hit...")

    hit_data = eval(request.data)
    new_hit = Hit(hit_data["time"], hit_data["player"])

    print("Hit created.")

    response = Response(status=200)

    print("Returning response (" + str(response) + ").")

    return response

@app.route("/stats/<player_id>", methods=["GET"])
def get_player_stats(player_id):
    print()
    print("Client requesting information...")
    print("Player ID: " + str(player_id))

    player_id = int(player_id)
    try:
        player = players[player_id]

        print("Player found. Generating response...")

        return_data = str({"id": player.id, "codename": player.codename,\
                           "health": player.health, "score": player.score})

        response = Response(return_data, status=200, mimetype="text/plain")
    except:
        print("Player not found. Alerting client...")

        response = Response(status=404)

    print("Returning response (" + str(response) + ").")

    return response
