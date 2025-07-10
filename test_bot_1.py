# Test bot 1 is a very simple bot that just places tiles in the first available spot
# in order to see that we can run a bot.

from helper.game import Game
from lib.interface.queries.typing import QueryType
from lib.interface.events.moves.typing import MoveType
from lib.interface.events.moves.move_place_tile import MovePlaceTile
from lib.interface.queries.query_place_tile import QueryPlaceTile
from lib.interface.queries.query_place_meeple import QueryPlaceMeeple
from lib.interface.events.moves.move_place_meeple import MovePlaceMeeple

class TestBot1:
    def __init__(self):
        pass

    def handle_place_tile(self, game: Game, query: QueryPlaceTile) -> MovePlaceTile:
        """Place a tile in the first available spot"""
        return game.move_place_tile(query, game.state.my_cards[0], 0)

    def handle_place_meeple(self, game: Game, query: QueryPlaceMeeple) -> MovePlaceMeeple:
        """Place a meeple in the first available spot"""
        return game.move_place_meeple(query, game.state.my_meeples[0], 0)

def main():
    game = Game()
    bot = TestBot1()

    while True:
        query = game.get_next_query()

        def choose_move(query: QueryType) -> MoveType:
            """Choose a move based on the query"""
            match query:
                case QueryPlaceTile() as q:
                    return bot.handle_place_tile(game, q)

                case QueryPlaceMeeple() as q:
                    return bot.handle_place_meeple(game, q)

        game.send_move(choose_move(query))

