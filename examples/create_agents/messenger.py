from __future__ import division
from builtins import range
import abce


class Messenger(abce.Agent):
    def init(self, simulation_parameters, agent_parameters):
        # your agent initialization goes here, not in __init__
        self.count = 1

    def messaging(self):
        max_firm = 2 ** self.round
        for id in range(max_firm):
            self.send(('firm', id), 'msg', id)

        max_hh = 2 ** self.round
        for id in range(max_hh):
            self.send(('household', id), 'msg', id)
