from helper.game import Game

from lib.interface.queries.typing import QueryType
from lib.interface.events.moves.typing import MoveType
from lib.interface.events.moves.move_place_tile import MovePlaceTile
from lib.interface.queries.query_place_tile import QueryPlaceTile


class BotState:
    def __init__(self):
        pass

def main():
    game = Game()
    bot_state = BotState()

    while True:
        query = game.get_next_query()


        def choose_move(query: QueryType) -> MoveType:
            match query:
                case QueryPlaceTile() as q:
                    return handle_place_tile(game, bot_state, q)

        game.send_move(choose_move(query))

