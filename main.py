from utils.constants import CWHITE, CGREENBG, CEND

from classes.Introduction import Introduction
from classes.hydraulic_performance.PerformanceMain import PerformanceMain
from classes.suitability_timeseries.SuitabilityTSMain import SuitabilityTSMain
from classes.ffc_result_metrics.FFCResultMetricsMain import FFCResultMetricsMain

selected_script = Introduction().script

# define all scripts into a dictionary
options = {
    'hydraulic_performance': PerformanceMain,
    'hydraulic_suitability_TS': SuitabilityTSMain,
    'ffc_result_metrics': FFCResultMetricsMain
}

# run select scripts
options[selected_script]()

print(CGREENBG + CWHITE + "Task Completed!" + CEND)
print("")
