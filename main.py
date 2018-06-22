from classes.hydraulic_performance.PerformanceMain import PerformanceMain
from classes.Introduction import Introduction

selected_script = Introduction().script

options = {
    'hydraulic performance': PerformanceMain,
}

options[selected_script]()
