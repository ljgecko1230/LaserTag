from flask import Flask, render_template, request

app = Flask(__name__)

players = []

class GameMode():
    def __init__(self):
        pass

class Player():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.team = None
        self.health = 100
        self.kills = 0
        self.deaths = 0

class Weapon():
    def __init__(self, id):
        self.id = id

def start_game():
    select_game_mode()
    add_players()
    generate_teams()

def select_game_mode():
    pass

def generate_teams():
    pass

@app.route("/", methods=["GET"])
def server_homepage():
    return render_template("home.html")

@app.route("/connect", methods=["POST"])
def join_game():
    player_data = eval(request.data.decode("utf-8"))
    new_player = Player(player_data["name"], len(players))
    players.append(new_player)

    return {"id": new_player.id}

@app.route("/shot", methods=["POST"])
def sent_shot():
    shot_data = eval(request.data.decode("utf-8"))
    return 1

@app.route("/hit", methods=["POST"])
def recieved_hit():
    hit_data = eval(request.data.decode("utf-8"))
    return 1
