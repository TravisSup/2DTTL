import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mp
import webbrowser




#Initialisation
def main():
    data = pd.read_csv('D:\\Documents\\Supinfo\\Cours\\Asc2\\2_DTTL\Projet_Final\\2DTTL\\weather_madrid.csv', sep=',', index_col=0)
    myDataFrame = pd.DataFrame(data)    
    fichier = open("D:\\Documents\\Supinfo\\Cours\\Asc2\\2_DTTL\Projet_Final\\2DTTL\\index.html", "a")
    fichier.write(myDataFrame.to_html(max_rows=10))
    fichier.close
    webbrowser.open("D:\\Documents\\Supinfo\\Cours\\Asc2\\2_DTTL\Projet_Final\\2DTTL\\index.html")


main()

