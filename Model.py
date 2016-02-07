__author__ = 'AmirHS'

import time


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
        self.__owner = -1
        self.__army_count = 0
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
    def __init__(self, queue):
        self.__turn_start_time = 0
        self.__turn_time_out = 400
        self.__queue = queue
        self.__turn = 0
        self.__my_id = 0
        self.__map = 0
        self.__nodes = [[], [], []]

    def handle_init_message(self, msg):
        self.__turn_time_out = int(msg[Constants.KEY_ARGS][0])
        self.__my_id = int(msg[Constants.KEY_ARGS][1])

        adj_list_init = msg[Constants.KEY_ARGS][2]
        nodes = []

        for i in range(len(adj_list_init)):
            nodes.append(Node(i))

        for i in range(len(adj_list_init)):
            #neighbours_int = adj_list_init[i]
            neighbours = []
            for j in adj_list_init[i]:
                neighbours.append(nodes[j])
            nodes[i].set_neighbours(neighbours)
        graph_diff = msg[Constants.KEY_ARGS][3]
        for i in range(len(graph_diff)):
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
        for i in range(len(graph_diff)):
            node_diff = graph_diff[i]
            node_index = int(node_diff[0])
            self.__map.get_node(node_index).set_owner(int(node_diff[1]))
            self.__map.get_node(node_index).set_army_count(int(node_diff[2]))
        self.__update_nodes_list()

    def __update_nodes_list(self):
        # dummies! :))
        nodes_list = [[],[],[]]
        for n in self.__map.get_nodes():
            nodes_list[n.get_owner() + 1].append(n)

        for i in range(len(self.__nodes)):
            self.__nodes[i] = nodes_list[i]
            #print(nodes_list[i], file=sys.stderr)

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
        self.__queue.put(Event('m', [src, dst, count]))


class Event:
    EVENT = "event"

    def __init__(self, type, args):
        self.type = type
        self.args = args

    def add_arg(self, arg):
        self.args.append(arg)

    #def to_message(self):
    #    return {
    #        'name': Event.EVENT,
    #        'args': [{'type': self.type, 'args': self.args}]
    #    }


class Constants:
    KEY_ARGS = "args"
    KEY_NAME = "name"

    CONFIG_KEY_IP = "ip"
    CONFIG_KEY_PORT = "port"
    CONFIG_KEY_TOKEN = "token"

    MESSAGE_TYPE_EVENT = "event"
    MESSAGE_TYPE_INIT = "init"
    MESSAGE_TYPE_SHUTDOWN = "shutdown"
    MESSAGE_TYPE_TURN = "turn"
