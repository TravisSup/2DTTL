import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mp
import webbrowser
import os




#Initialisation
def main():
    os.chdir(os.path.dirname (__file__))
    data = pd.read_csv('weather_madrid.csv', sep=',', index_col=0) #reads the csv file and stores the content into a variable 
    myDataFrame = pd.DataFrame(data) #creates a 2-dimensional data structure from the variable where the data from the csv file were stored
    fichier = open("index.html", "w")
    fichier.write(myDataFrame.to_html(max_rows=10))
    fichier.close
    webbrowser.open("index.html")


main()

