from flask import Flask, render_template, request

app = Flask(__name__)

players = []

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
    def __init__(self, id, time, player):
        self.id = id
        self.time = time
        self.player = player

class Shot(Event):
    pass

class Hit(Event):
    pass

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def login():
    pass

@app.route("/shot")
def recieve_shot():
    pass

@app.route("/hit")
def recieve_hit():
    pass
