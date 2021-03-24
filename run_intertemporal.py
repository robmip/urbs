import os
import shutil
import urbs
#import date
#import datetime
from datetime import date, datetime
#from datetime import datetime

print(f'initiate run: {datetime.now()}')

input_files = 'Intertemporal_example'  # for single year file name, for intertemporal folder name
input_dir = 'Input'
input_path = os.path.join(input_dir, input_files)

result_name = 'Intertemp'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

print(f'Data prepared and read: {datetime.now()}')
#get year
year = date.today().year

# copy input file to result directory
try:
    shutil.copytree(input_path, os.path.join(result_dir, input_dir))
except NotADirectoryError:
    shutil.copyfile(input_path, os.path.join(result_dir, input_files))
# copy run file to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost'  # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'glpk'

# simulation timesteps
(offset, length) = (0, 27)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sites
report_tuples = [
    #(year, 'North', 'Elec'),
    #(year, 'Mid', 'Elec'),
    #(year, 'South', 'Elec'),
    #(year, ['North', 'Mid', 'South'], 'Elec'),
    #(year+5, 'North', 'Elec'),
    #(year+5, 'Mid', 'Elec'),
    #(year+5, 'South', 'Elec'),
    #(year+5, ['North', 'Mid', 'South'], 'Elec'),
    #(year+10, 'North', 'Elec'),
    #(year+10, 'Mid', 'Elec'),
    #(year+10, 'South', 'Elec'),
    #(year+10, ['North', 'Mid', 'South'], 'Elec'),
    #(year+15, 'North', 'Elec'),
    #(year+15, 'Mid', 'Elec'),
    #(year+15, 'South', 'Elec'),
    #(year+15, ['North', 'Mid', 'South'], 'Elec'),    
    ]

# optional: define names for sites in report_tuples
report_sites_name = {
    #('North', 'Mid', 'South'): 'All'
    }

# plotting commodities/sites
plot_tuples = [
    #(year, 'North', 'Elec'),
    #(year, 'Mid', 'Elec'),
    #(year, 'South', 'Elec'),
    #(year, ['North', 'Mid', 'South'], 'Elec'),
    #(year+5, 'North', 'Elec'),
    #(year+5, 'Mid', 'Elec'),
    #(year+5, 'South', 'Elec'),
    #(year+5, ['North', 'Mid', 'South'], 'Elec'),
    #(year+10, 'North', 'Elec'),
    #(year+10, 'Mid', 'Elec'),
    #(year+10, 'South', 'Elec'),
    #(year+10, ['North', 'Mid', 'South'], 'Elec'),
    #(year+15, 'North', 'Elec'),
    #(year+15, 'Mid', 'Elec'),
    #(year+15, 'South', 'Elec'),
    #(year+15, ['North', 'Mid', 'South'], 'Elec'),    
    ]

# optional: define names for sites in plot_tuples
plot_sites_name = {('North', 'Mid', 'South'): 'All'}

# plotting timesteps
plot_periods = {
    'all': timesteps[1:]
}

# add or change plot colors
my_colors = {
    #Cen:
    #Car:
    #Nor:
    #Ori:
    #Val:
    #'South': (230, 200, 200),
    #'Mid': (200, 230, 200),
    #'North': (200, 200, 230)
    }
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base,
             #urbs.scenario_co2_tax,
             #urbs.scenario_high_biom
             #urbs.scenario_stock_prices,
             #urbs.scenario_co2_limit,
             #urbs.scenario_no_dsm,
             #urbs.scenario_north_process_caps,
             #urbs.scenario_all_together
            ]
print(f'solving and reporting: {datetime.now()}')

for scenario in scenarios:
    prob = urbs.run_scenario(input_path, solver, timesteps, scenario,
                             result_dir, dt, objective,
                             plot_tuples=plot_tuples,
                             plot_sites_name=plot_sites_name,
                             plot_periods=plot_periods,
                             report_tuples=report_tuples,
                             report_sites_name=report_sites_name)
