from utils.constants import CWHITE, CGREENBG, CEND

from classes.Introduction import Introduction
# hydraulic suitability
from classes.hydraulic_suitability.HydraulicSuitabilityMain import HydraulicSuitabilityMain
from classes.suitability_timeseries.SuitabilityTSMain import SuitabilityTSMain
from classes.ffc_result_metrics.FFCResultMetricsMain import FFCResultMetricsMain

# performance metrics
from classes.performance_metric.PerformanceMetricMain import PerformanceMetricMain

selected_script = Introduction().script

# define all scripts into a dictionary
options = {
    'hydraulic_suitability': HydraulicSuitabilityMain,
    'hydraulic_suitability_TS': SuitabilityTSMain,
    'ffc_result_metrics': FFCResultMetricsMain,
    'performance_metrics': PerformanceMetricMain
}

# run select scripts
options[selected_script]()

print(CGREENBG + CWHITE + "Task Completed!" + CEND)
print("")
