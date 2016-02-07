__author__ = 'AmirHS'

import json
import time, sys


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


class World:
    def __init__(self, sender):
        self.__turn_start_time = 0
        self.__turn_time_out = 400
        self.__sender = sender
        self.__turn
        self.__my_id
        self.__map
        self.__nodes

    def handle_init_message(self, msg):
        self.__turn_time_out = int(msg[Constants.KEY_ARGS][0])
        self.__my_id = int(msg[Constants.KEY_ARGS][1])

        adj_list_init = msg[Constants.KEY_ARGS][2]
        nodes = []

        for node in adj_list_init:
            nodes.append(Node(node))

        for i in range(0, adj_list_init.size()):
            neighbours_int = adj_list_init[i]
            neighbours = []
            for j in range(0, adj_list_init[i].size):
                neighbours[j] = nodes[int(neighbours_int[j])]
            nodes[i].set_neighbours(neighbours)
        graph_diff = msg[Constants.KEY_ARGS][3]
        for i in range(0, graph_diff.size()):
            node_diff = graph_diff[i]
            node = int(node_diff[0])
            owner = int(node_diff[1])
            army_count = int(node_diff[2])
            nodes[node].set_owner(owner)
            nodes[node].set_army_count(army_count)
        self.__map = Graph(nodes)
        self.__update_nodes_list()

    def handle_turn_message(self, msg):
        self.__turn_start_time = int(round(time.time()*1000))
        self.__turn = int(msg[Constants.KEY_ARGS][0])

        graph_diff = msg[Constants.KEY_ARGS][1]
        for i in range(0, graph_diff.size()):
            node_diff = graph_diff[i]
            node_index = int(node_diff[0])
            self.__map.get_node(node_index).set_owner(int(node_diff[1]))
            self.__map.get_node(node_index).set_army_count(int(node_diff[2]))
        self.__update_nodes_list()

    def __update_nodes_list(self):
        # dummies! :))
        nodes_list = [3]
        nodes_list[0] = []
        nodes_list[1] = []
        nodes_list[2] = []
        for n in self.__map.get_nodes():
            nodes_list[n.get_owner() + 1].append(n)

        for i in range(0, self.__nodes):
            self.__nodes[i] = nodes_list[i]
            print(nodes_list[i], file=sys.stderr)

    def get_turn_time_passed(self):
        return int(round(time.time()*1000)) - self.__turn_start_time

    def get_turn_remaining_time(self):
        return self.__turn_time_out - self.get_turn_time_passed()

    def get_my_id(self):
        return self.__my_id

    def get_map(self):
        return self.__map

    def get_my_nodes(self):
        return self.__nodes[self.__my_id + 1]

    def get_opponent_nodes(self):
        return self.__nodes[2 - self.__my_id]

    def get_free_nodes(self):
        return self.__nodes[0]

    def get_turn_number(self):
        return self.__turn

    def get_total_turn_time(self):
        return self.__turn_time_out

    def move_army(self, src, dst, count):
        self.__sender.accept(Event.EVENT, Event('m', [src, dst, count]))


class Event:
    EVENT = "event"

    def __init__(self, type, args):
        self.type = type
        self.args = args

    def add_arg(self, arg):
        self.args.append(arg)

    def to_message(self):
        return {
            'name': Event.EVENT,
            'args': [{'type': self.type, 'args': self.args}]
        }


class Constants:
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
