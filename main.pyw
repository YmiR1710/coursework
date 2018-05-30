from visualisation import Visualization
from data_work import analise_data

try:
    Visualization.visualize_1() #creating a window for choice of genres
    Visualization.updater() #searching for information
    Visualization.visualize_2(analise_data(Visualization.films_list)) #analysis of information
except:
    Visualization.visualize_2("ERROR")
