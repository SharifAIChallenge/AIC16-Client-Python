__author__ = 'AmirHS'


class AI():
    def do_turn(self, world):
        my_nodes = world.get_my_nodes()
        for n in my_nodes:
            for nn in n.neighbours:
                if nn.owner != world.my_id:
                    world.move_army(n.index, nn.index, int(n.army_count / 2))
