from visualisation import Visualization
from data_work import analise_data

try:
    Visualization.visualize_1()
    Visualization.updater()
    Visualization.visualize_2(analise_data(Visualization.films_list))
except:
    Visualization.visualize_2("ERROR")
