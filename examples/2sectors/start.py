""" Agents are now build according
to the line in agents_parameter.csv
"""
from abce import Simulation, gui
from firm import Firm
from household import Household


simulation_parameters = {'name': 'name',
                         'trade_logging': 'off',
                         'random_seed': None,
                         'rounds': 10}

#@gui(simulation_parameters)


def main(simulation_parameters):
    w = Simulation()
    w.declare_round_endowment(resource='labor_endowment', units=5, product='labor')
    w.declare_perishable(good='labor')

    firms = w.build_agents(Firm, 'firm', 2)
    households = w.build_agents(Household, 'household', 2)

    for r in range(simulation_parameters['rounds']):
        w.advance_round(r)
        # to access round, just get the value of w.round
        # to access its datetime version, use w._round # todo, better naming
        households.sell_labor()
        firms.buy_inputs()
        firms.production()
        firms.panel_log(possessions=['consumption_good', 'intermediate_good'])
        firms.sell_intermediary_goods()
        households.buy_intermediary_goods()
        households.panel_log(possessions=['consumption_good'])
        households.consumption()
    w.finalize()


if __name__ == '__main__':
    main(simulation_parameters)
