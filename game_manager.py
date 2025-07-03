from player import *


class GameManager:
    def __init__(self):
        # Store player objects in a private dict: name -> Player instance
        self._players = {}

    def make_players(self, list_of_players: set) -> None:
        for name in list_of_players:
            self._players[name] = Player(name)

    def get_player(self, name) -> Player:
        return self._players.get(name)

    def get_all_players(self) -> list:
        return list(self._players.values())
