# Imports

class Adjudicator:
    """
    Class to compare and rank players and their relative hands.
    """

    @staticmethod
    def comparitor(players: list) -> dict:
        """
        Compares the list of players and scores and returns them in order of rank.
        """
        # Sort players by their scores, descending
        sorted_players = sorted(players, key=lambda p: p.get_player_score(), reverse=True)

        # Build a rank dictionary
        rank_dict = {rank: player.player_name for rank, player in enumerate(sorted_players, start=1)}

        return rank_dict

