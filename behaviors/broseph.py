from typing import NamedTuple
from typing import List
import sqlite3
import math
import numpy


class Coordinates(NamedTuple):
    x: int
    y: int


class Size(Coordinates):
    pass


class Origin:
    def __init__(self, dna: dict):
        self.x, self.y = Coordinates(dna.get("init_pos"))


class ScreenSize:
    def __init__(self, dna: dict):
        self.width: int = dna.get("MAX_X")
        self.height: int = dna.get("MAX_Y")


class FlagPosition:
    def __init__(self, dna: dict):
        self.x, self.y = Coordinates(dna.get("flag_x_y"))


class SurfBro:
    def __init__(
        self, dna: dict, id: str, state: dict, cursor: sqlite3.Cursor
    ):
        self.id = id
        self.__state = state
        self.__dna = dna
        self.__cursor = cursor

    @property
    def origin(self) -> Coordinates:
        return Coordinates(*self.__dna.get("init_pos"))

    @property
    def screen_size(self) -> Size:
        return Size(self.__dna.get("MAX_X"), self.__dna.get("MAX_Y"))

    @property
    def home_base(self) -> Coordinates:
        return Coordinates(*self.__dna.get("flag_x_y"))

    @property
    def location_history(self) -> List[Coordinates]:
        if history := self.__state.get("location_history", None):
            return history
        else:
            self.__state["location_history"] = []
            return self.__state.get("location_history")

    def update_location_history(self, location: Coordinates):
        self.location_history.append(location)

    @property
    def current_location(self) -> Coordinates:
        return Coordinates(
            *self.__cursor.execute(
                f"""
                SELECT x, y FROM main_game_field WHERE is_flag = FALSE and d_id = '{self.id}'
                """
            ).fetchone()
        )

    def update_location(self, location: Coordinates):
        self.__cursor.execute(
            f"""
            INSERT INTO engine_orders VALUES (
                {self.current_location.x},
                {self.current_location.y},
                {location.x}, {location.y},
                'MOVE', '{self.id}'
            )"""
        )
        self.update_location_history(location=location)


class BoardMaster:
    def __init__(self, db_cursor: sqlite3.Cursor, surf_bro: SurfBro):
        self.__cursor = db_cursor
        self.__surf_bro = surf_bro

    @property
    def food_locations(self) -> List[Coordinates]:
        return [
            Coordinates(*coordinates)
            for coordinates in self.__cursor.execute(
                """
                SELECT x,y from main_game_field WHERE is_flag = FALSE and owner_id = 0;
                """
            ).fetchall()
        ]

    def closest_distance(self, targets: List[Coordinates]):
        source = self.__surf_bro.current_location
        # if not len(targets) > 0:
        #     return -1
        return numpy.argmin(
            [
                math.sqrt(
                    math.pow((source.x - target.x), 2)
                    + math.pow((source.y - target.y), 2)
                )
                for target in targets
            ]
        )

    def closest_food(self) -> Coordinates:
        index = self.closest_distance(self.food_locations)
        # if index > -1:
        return self.food_locations[index]
        # return self.__surf_bro.home_base


def update(dna, d_id, state, db_cursor):
    bro = SurfBro(dna, d_id, state, db_cursor)
    board_master = BoardMaster(db_cursor, bro)

    current_location = bro.current_location

    if len(board_master.food_locations) > 0:
        destination = board_master.closest_food()
        destination = Coordinates(
            destination.x - current_location.x,
            destination.y - current_location.y,
        )
    else:
        destination = bro.home_base

    # with open("hangry.txt", "a+") as f:
    #     f.write(
    #         f"""bro.enemy_locations ==> {board_master.enemy_locations}\n\n"""
    #         # bro.historical_locations ==> {bro.location_history}
    #         # bro.origin ==> {bro.origin}
    #         # bro.screen_size ==> {bro.screen_size}
    #         # bro.home_base ==> {bro.home_base}
    #         # bro.current_location ==> {bro.current_location}
    #         # board_master.closest_food ==> {closest_food}\n\n
    #     )

    dx, dy = (0, 0)
    if destination.x < 0:
        dx = -1
    if destination.x > 0:
        dx = 1
    if destination.y < 0:
        dy = -1
    if destination.y > 0:
        dy = 1

    new_location = Coordinates(
        x=bro.current_location.x + dx, y=bro.current_location.y + dy
    )
    bro.update_location(location=new_location)
