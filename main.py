from utils.constants import CWHITE, CGREENBG, CEND

from classes.Introduction import Introduction
from classes.hydraulic_performance.PerformanceMain import PerformanceMain
from classes.suitability_timeseries.SuitabilityTSMain import SuitabilityTSMain

selected_script = Introduction().script

# define all scripts into a dictionary
options = {
    'hydraulic_performance': PerformanceMain,
    'hydraulic_suitability_TS': SuitabilityTSMain,
}

# run select scripts
options[selected_script]()

print(CGREENBG + CWHITE + "Task Completed!" + CEND)
print("")
