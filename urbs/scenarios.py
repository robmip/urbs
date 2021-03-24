import pandas as pd

# SCENARIO GENERATORS
# In this script a variety of scenario generator functions are defined to
# facilitate scenario definitions.


def scenario_base(data):
    # do nothing
    return data


def scenario_stock_prices(data):
    # change stock commodity prices
    co = data['commodity']
    stock_commodities_only = (co.index.get_level_values('Type') == 'Stock')
    co.loc[stock_commodities_only, 'price'] *= 1.5
    return data


def scenario_co2_limit(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] *= 0.05
    return data


def scenario_co2_tax(data):
    # change CO2 price in Mid
    co = data['commodity']
    #for stf in data['global_prop'].index.levels[0].tolist():
    co.loc[('Cen', 'CO2', 'Env'), 'price'] = 100
    co.loc[('Car', 'CO2', 'Env'), 'price'] = 100
    co.loc[('Nor', 'CO2', 'Env'), 'price'] = 100
    co.loc[('Ori', 'CO2', 'Env'), 'price'] = 100
    co.loc[('Val', 'CO2', 'Env'), 'price'] = 100
    return data

def scenario_high_biom(data):
    # change CO2 price in Mid
    co = data['suplm']
    #for stf in data['global_prop'].index.levels[0].tolist():
    co['Cen.Bagasse'] *= .3
    co['Ori.Bagasse'] *= .3
    co['Nor.Bagasse'] *= .3
    co['Val.Bagasse'] *= .3
    return data

def scenario_north_process_caps(data):
    # change maximum installable capacity
    pro = data['process']
    for stf in data['global_prop'].index.levels[0].tolist():
        pro.loc[(stf, 'North', 'Hydro plant'), 'cap-up'] *= 0.5
        pro.loc[(stf, 'North', 'Biomass plant'), 'cap-up'] *= 0.25
    return data


def scenario_no_dsm(data):
    # empty the DSM dataframe completely
    data['dsm'] = pd.DataFrame()
    return data


def scenario_all_together(data):
    # combine all other scenarios
    data = scenario_stock_prices(data)
    data = scenario_co2_limit(data)
    data = scenario_north_process_caps(data)
    return data
