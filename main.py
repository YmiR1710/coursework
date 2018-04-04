from progress_tester import Visualization
from films import search

try:
    Visualization.visualize_1()
    Visualization.updater()
except:
    Visualization.visualize_2("ERROR")
