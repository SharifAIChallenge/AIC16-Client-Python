__author__ = 'amirHS'

import json


class Graph:
    def __init__(self, nodes):
        self.__nodes = nodes

    def get_nodes(self):
        return self.__nodes

    def get_node(self, i):
        return self.__nodes[i]


class Node:
    def __init__(self, index):
        self.__index = index
        self.__index
        self.__owner
        self.__army_count
        self.__neighbours = []

    def get_neighbours(self):
        return self.__neighbours

    def get_index(self):
        return self.__index

    def get_owner(self):
        return self.__owner

    def get_army_count(self):
        return self.__army_count

    def set_neighbours(self, neighbours):
        self.__neighbours = neighbours

    def set_owner(self, owner):
        self.__owner = owner

    def set_army_count(self, army_count):
        self.__army_count = army_count

    def set_index(self, index):
        self.__index = index


class Message:
    def __init__(self, name, args):
        self.name = name
        self.args = json.loads(args)


class World:
    __turn_time_out = 400
    __turn_start_time = 0
    __events = []

    def __init__(self, sender):
        self.__sender = sender

    def handle_init_message(self, msg):
        self.__turn_time_out = long(msg.args.get(0))
        self.my_id = int(msg.args.get(1))


class Constants():
    class Directions:
        NORTH = "NORTH"
        NORTH_EAST = "NORTH_EAST"
        SOUTH_EAST = "SOUTH_EAST"
        SOUTH = "SOUTH"
        SOUTH_WEST = "SOUTH_WEST"
        NORTH_WEST = "NORTH_WEST"

    DIRECTIONS = [
        Directions.NORTH, Directions.NORTH_EAST, Directions.SOUTH_EAST,
        Directions.SOUTH, Directions.SOUTH_WEST, Directions.NORTH_WEST,
    ]

    KEY_ID = "id"
    KEY_TURN = "turn"
    KEY_ARGS = "args"
    KEY_NAME = "name"
    KEY_OTHER = "other"
    KEY_TYPE = "type"
    KEY_TEAM_ID = "teamId"
    KEY_STATICS = "statics"
    KEY_DYNAMICS = "dynamics"
    KEY_TRANSIENTS = "transients"

    BLOCK_TYPE_NONE = "n"
    BLOCK_TYPE_NORMAL = "o"
    BLOCK_TYPE_MITOSIS = "m"
    BLOCK_TYPE_RESOURCE = "r"
    BLOCK_TYPE_IMPASSABLE = "i"

    BLOCK_KEY_TURN = "t"
    BLOCK_KEY_TYPE = "y"
    BLOCK_KEY_JUMP_IMP = "j"
    BLOCK_KEY_HEIGHT = "h"
    BLOCK_KEY_ATTACK_IMP = "a"
    BLOCK_KEY_RESOURCE = "r"
    BLOCK_KEY_MIN_HEIGHT = "m"
    BLOCK_KEY_DEPTH_OF_FIELD_IMP = "d"
    BLOCK_KEY_GAIN_RATE_IMP = "g"

    CELL_KEY_JUMP = "j"
    CELL_KEY_ENERGY = "e"
    CELL_KEY_ATTACK = "a"
    CELL_KEY_VISIBLE = "v"
    CELL_KEY_DEPTH_OF_FIELD = "d"
    CELL_KEY_GAIN_RATE = "g"

    GAME_OBJECT_TYPE_CELL = "c"
    GAME_OBJECT_TYPE_DESTROYED = "d"

    GAME_OBJECT_KEY_OBJECT_ID = "objectId"
    GAME_OBJECT_KEY_ID = "i"
    GAME_OBJECT_KEY_TURN = "t"
    GAME_OBJECT_KEY_TYPE = "y"
    GAME_OBJECT_KEY_OTHER = "o"
    GAME_OBJECT_KEY_TEAM_ID = "ti"
    GAME_OBJECT_KEY_DURATION = "d"
    GAME_OBJECT_KEY_POSITION = "p"

    INFO_KEY_TURN = "turn"
    INFO_KEY_TEAMS = "teams"
    INFO_KEY_VIEWS = "views"
    INFO_KEY_YOUR_INFO = "yourInfo"
    INFO_KEY_MAP_SIZE = "mapSize"
    INFO_KEY_BLOCK_COEFFICIENT = "blockCoefficient"

    MESSAGE_TYPE_EVENT = "event"
    MESSAGE_TYPE_INIT = "init"
    MESSAGE_TYPE_SHUTDOWN = "shutdown"
    MESSAGE_TYPE_TURN = "turn"

    CONFIG_KEY_IP = "ip"
    CONFIG_KEY_PORT = "port"
    CONFIG_KEY_TOKEN = "token"

    MAP_SIZE_HEIGHT = "height"
    MAP_SIZE_WIDTH = "width"

    BLOCK_MAX_HEIGHT = 9

    CELL_MAX_DEPTH_OF_FIELD = 5
    CELL_MAX_GAIN_RATE = 45
    CELL_MAX_ATTACK = 35
    CELL_MAX_JUMP = 5
    CELL_MIN_ENERGY_FOR_MITOSIS = 80
    CELL_MAX_ENERGY = 100
