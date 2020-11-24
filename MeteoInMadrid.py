import os
import webbrowser as wb
import matplotlib as mp
import numpy as np
import pandas as pd
import seaborn as sb


def narrowSelection(dataToStudy):  
    print("\nRenommage des attribut : \n")
    print(dataToStudy) #Displays the dataframe
    print("\nDétail des données : \n")
    print(dataToStudy.describe()) #Applies the describe method to the dataframe and displays it
    print("\nDétail des 'events' : \n")
    print(dataToStudy["Events"].describe()) #Applies the describe method to the Events attribute of the dataframe and displays it
    print("\nL'attribut présentant une anomalie est la température")
    sb.boxplot(data=dataToStudy["MaxTemp"].describe(), showfliers = False) #Applies the describe method to the MaxTemp attribute of the dataframe and displays it while removing flier from the graph
    mp.pyplot.show()



def cleaningData(dataToStudy): 
    print("""\nNous avons retenu les valeurs suivantes à enlever de notre série de donnée : \n 
    - La température maximum atteinte (80°C) \n
    - Le nombre de valeurs (Il n'y a pas lieu de l'afficher sur le Boxplot.De plus, si nous l'affichons, cette valeur sera un outflier)\n""") #Displays Text

    #sb.boxplot(data=dataToStudy["MaxTemp"].describe(), showfliers = False) #Applies the describe method to the MaxTemp attribute of the dataframe and displays it while removing flier from the graph
    #mp.pyplot.show()
    
    cleanedData = dataToStudy.drop(dataToStudy["MaxTemp"].idxmax())
    sb.boxplot(data=cleanedData.describe(), showfliers = False) #Applies the describe method to the MaxTemp attribute of the dataframe and displays it while removing flier from the graph   
    mp.pyplot.show()

    print("\nSans dropna : ")
    print (dataToStudy.isnull().sum()) #Makes th summ of the null values present in the dataFrame
    print("\nAvec dropna : ")
    print(dataToStudy.dropna().isnull().sum()) #Makes th summ of the null values present in the dataFrame after the removing of Nan values
    print("La fonction dropna supprime les valeurs Nan de la dataFrame")
    print("""La fonction dropna n'est pas pertinente à utiliser dans notre cas car elle fausse nos résultats statistique, 
    elle diminue le nombre de donnée composant la série ce qui faussera les analyse.""")

    print("\nOui il y a des valeurs null qui sont au nombre de : ")    
    numberOfNanValue = 0
    for content in dataToStudy.drop(["date"], axis=1).isnull().sum(): # loop that displays the sum of the Nan values for each column where there are some
        numberOfNanValue+=content    
    print(numberOfNanValue) #Displays Text

    print("\n Remplacement de tout les NaN dans l'attribut 'Events' par NoEvent : ")
    dataToStudy["Events"].fillna('NoEvent', inplace = True)
    print(dataToStudy)
    
    print("""\n Remplacement de tous les NaN dans les attributs 'Temperature, Humididty, Dew, CloudCover' par 
    la valeur moyenne signifiant que c'était un jour 'normal'(il ne s'est rien passé d'extraordinaire) : """)
    
   
    temp = dataToStudy.drop(["date", "Events"] ,axis=1)
    
    for element in temp.columns:
        dataToStudy[element].fillna(temp[element].mean(), inplace=True)

    print("\nLes valeurs NaN restantes : ")
    print (dataToStudy.isnull().sum())
    


def dateProcessing(dataToStudy):
# Question 6.1: Utilisez la fonction to_datetime() pour convertir la chaîne en une date. Utilisez la fonction dtypes pour vérifier si la conversion a été correctement effectuée.

    print("\n reformatage des dates : ")
    print(dataToStudy["date"])
    dataToStudy['date'] = pd.to_datetime(dataToStudy["date"]) #converting the character date chain to a value of type "date"
    print(dataToStudy["date"])

    print("\nConversion de la chaîne de caractère en valeur de type 'date' :")
    print(dataToStudy.select_dtypes(include='datetime').columns)


# Question 6.2 / 6.3  Ajouter un nouvel attribut "year"/"day" contenant (l'année / le jour) de la date sous forme d'entier

    dataToStudy['year'] = dataToStudy['date'].dt.year #Creates an attribute called year based of the 
    dataToStudy['day'] = dataToStudy['date'].dt.day

    print(dataToStudy)

# Question 6.4 : Écrivez les données résultantes dans un fichier nommé weather_madrid_clean.csv.

    dataToStudy.to_csv('weather_madrid_preocessed.csv') #Creates a csv file from the dataToStudy dataframe

#Initialisation
def main():
    os.chdir(os.path.dirname (__file__)) #redefine the workspace in wich the python file is run
    data = pd.read_csv('weather_madrid.csv', sep=',') #reads the csv file and stores the content into a variable
    myDataFrame = pd.DataFrame(data) #creates a data frame structure with the data from the csv file contained in the data variable
    fichier = open("index.html", "w") #opens / creates a file if he doesn't exist 
    fichier.write(myDataFrame.to_html(max_rows=10)) #writes the first 10 rows from the data wich contains the csv data into the html file 
    fichier.close() #stops the writing of new data into the html file
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
        print("Yes, there are some NaN elements") #print yes if there are null values
    

    dataToStudy = pd.DataFrame(data= data, columns=["CET", "Mean TemperatureC", "Min TemperatureC", "Max TemperatureC", "Mean Humidity", "Max Humidity", "Min Humidity", "MeanDew PointC", "Min DewpointC", "Dew PointC", "CloudCover", "Events"]) #creates a new dataframe based 
    dataToStudy.rename(columns = {"CET":"date", "Mean TemperatureC":"Meantemp","Min TemperatureC":"MinTemp","Max TemperatureC":"MaxTemp","Mean Humidity":"MeanHum","Max Humidity":"MaxHum","Min Humidity":"MinHum","MeanDew PointC":"MeanDew","Min DewpointC":"MinDew","Dew PointC":"Dew",}, inplace = True) #Renames
    #the attributes
    narrowSelection(dataToStudy)
    cleaningData(dataToStudy)
    dateProcessing(dataToStudy)



main() #runs the "main" method
