import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mp
import webbrowser as wb
import os



#Initialisation
def main():
    os.chdir(os.path.dirname (__file__)) #redefine the workspace in wich the python file is run
    data = pd.read_csv('weather_madrid.csv', sep=',', index_col=0) #reads the csv file and stores the content into a variable 
    myDataFrame = pd.DataFrame(data) #creates a data frame structure with the data from the csv file contained in the data variable
    fichier = open("index.html", "w") #opens / creates a file if he doesn't exist 
    fichier.write(myDataFrame.to_html(max_rows=10)) #writes the first 10 rows from the data wich contains the csv data into the html file 
    fichier.close #stops the writing of new data into the html file
    wb.open("index.html")

    numericAttribute = myDataFrame.select_dtypes(include='number').columns #creates a series that contains the name of the attributes/columns that are filled with the type number 
    nonNumericAttribute = myDataFrame.select_dtypes(include='object').columns #creates a series that contains the name of the attributes/columns that are filled with the type strings 
    
    allElement = "" #creates a variable 
    for element in numericAttribute: #iterates through the numericAttribute series
        allElement += element+", "  #add each elements of the series and adds it to the string "allElements"
    print("Numeric attribute : "+allElement) #Displays each element into the console
    print("\n")
    for element in nonNumericAttribute: #iterates through the nonNumericAttribute series
        print("String attribute : "+element)  #Displays each element into the console

    
    temp = myDataFrame.isnull().any() #creates a series that returns true or false based of if there are null values in the data
    if not(temp.all()): #checks if there are 'True'statements in the series temps which signifies that there are null values in the csv file
        print("yes") #print yes if there are null values
    
    

main() #runs the "main" method

