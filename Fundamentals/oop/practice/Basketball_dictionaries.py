class player:
    def __init__(self, obj):
        self.name = obj['name']
        self.age = obj['age']
        self.position = obj['position']
        self.team = obj['team']
    
     # NINJA BONUS class mehotd
    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects

    
    def __repr__(self):
      display=f"\n player: {self.name},age {self.age} , pos: {self.position}, team: {self.team} \n"
      return display


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}
player_kevin = player(kevin)
player_jason = player(jason)
player_kyrie = player(kyrie)
print(player_jason)
print(player_kyrie)
print(player_kevin)


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",         "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

new_team = []
for obj in players:
     new=player(obj)
     new_team.append(new)
     print(new_team)

