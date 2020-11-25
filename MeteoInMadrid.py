# Question 1.1 : Initialiser l'environnement pandas, numpy, seaborn et matplotlib.pylot.
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


# Question 4.3 : Utilisez la fonction describe() pour voir les détails de vos données filtrées. Observez les informations et trouvez l'aberration.
    sb.boxplot(data=dataToStudy["MaxTemp"].describe(), showfliers = False) #Applies the describe method to the MaxTemp attribute of the dataframe and displays it while removing flier from the graph
    mp.pyplot.show()


def cleaningData(dataToStudy): 

# Question 4.4 : Quel attribut présente une anomalie ?
    print("""\nNous avons retenu les valeurs suivantes à enlever de notre série de donnée : \n 
    - La température maximum atteinte (80°C) \n
    - Le nombre de valeurs (Il n'y a pas lieu de l'afficher sur le Boxplot.De plus, si nous l'affichons, cette valeur sera un outflier)\n""") #Displays Text

    
#Question 4.5 Utilisez Seaborn pour tracer un boxplot de l'attribut anormal. Qu'observez-vous ? Combien y a-t-il de valeurs aberrantes ?
    sb.boxplot(data=dataToStudy) 
    mp.pyplot.show()
    
#Question 5.1 Traiter les valeurs aberrantes : Corriger le(s) point(s) aberrant(s) et expliquer votre choix.
    filtDataToStudy = dataToStudy.drop(["Events", "date"], axis=1) #creates a new dataFrame without the events and Date attribute
    quantFiltDataToStudy = filtDataToStudy.quantile([0.25, 0.75]) #Calculate the quartiles for the different attributes
    filtDataToStudy = filtDataToStudy.apply(lambda x: x[(x>quantFiltDataToStudy.loc[0.25,x.name]-1.5*(quantFiltDataToStudy.loc[0.75, x.name]-quantFiltDataToStudy.loc[0.25, x.name]))\
         & (x<quantFiltDataToStudy.loc[0.25,x.name]+1.5*(quantFiltDataToStudy.loc[0.75, x.name]-quantFiltDataToStudy.loc[0.25, x.name]))])
    cleanedData = pd.concat([dataToStudy.date, filtDataToStudy, dataToStudy.Events]) #Applies the formula to remove aberrant data from the graph
    sb.boxplot(data=cleanedData) #Applies the describe method to the MaxTemp attribute of the dataframe and displays it while removing flier from the graph   
    mp.pyplot.show() #Displays the graph 

# Question 5.3 : Que se passe-t-il si vous utilisez la fonction dropna() ?
    print("\nSans dropna : ")
    print (dataToStudy.isnull().sum()) #Makes th summ of the null values present in the dataFrame
    print("\nAvec dropna : ")
    print(dataToStudy.dropna().isnull().sum()) #Makes th sum of the null values present in the dataFrame after the removing of Nan values
    print("La fonction dropna supprime les valeurs Nan de la dataFrame")
# Question 5.4 : Pensez-vous que c'est une bonne idée d'utiliser la fonction dropna()   
    print("""La fonction dropna n'est pas pertinente à utiliser dans notre cas car elle fausse nos résultats statistique, 
    elle diminue le nombre de donnée composant la série ce qui faussera les analyse.""")

# Question 5.5 : Avez-vous des valeurs manquantes pour l'attribut "Events" ? Combien ?
    print("\nOui il y a des valeurs null qui sont au nombre de : ")    
    numberOfNanValue = 0
    for content in dataToStudy.drop(["date"], axis=1).isnull().sum(): # loop that displays the sum of the Nan values for each column where there are some
        numberOfNanValue+=content    
    print(numberOfNanValue) #Displays Text

# Question 5.6 : Remplacez tous les événements NaN par "NoEvent" pour indiquer qu'aucun événement ne s'est produit.
    print("\n Remplacement de tout les NaN dans l'attribut 'Events' par NoEvent : ")
    dataToStudy["Events"].fillna('NoEvent', inplace = True)
    print(dataToStudy)

# Question 5.7 : Expliquez votre choix lorsque vous remplissez toutes les valeurs manquantes.
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

# Question 1.2 : Créer une variable d’utilisation nommée data à partir de l'import des données de weather_madrid.csv. 
    data = pd.read_csv('weather_madrid.csv', sep=',') #reads the csv file and stores the content into a variable


# Question 2.1 : Créer une page de vue des données en html. Vous pouvez limiter votre page à quelques lignes.
    fichier = open("index.html", "w") #opens / creates a file if he doesn't exist 
    fichier.write(data.to_html(max_rows=10)) #writes the first 10 rows from the data wich contains the csv data into the html file 
    fichier.close() #stops the writing of new data into the html file


# Question 2.2 : Faites une instruction pour ouvrir votre page web html de la question 2.1 dans un navigateur.
    wb.open("index.html")

# Question 3.1 / 3.2 : Quels sont les attributs numériques (quantitatifs) et les attributs qui ne sont pas numériques (cathégoriques) ?
    numericAttribute = data.select_dtypes(include='number').columns #creates a series that contains the name of the attributes/columns that are filled with the type number 
    nonNumericAttribute = data.select_dtypes(include='object').columns #creates a series that contains the name of the attributes/columns that are filled with the type strings 
    
    allElement = "" #creates a variable 
    for element in numericAttribute: #iterates through the numericAttribute series
        allElement += element+", "  #add each elements of the series and adds it to the string "allElements"
    print("Numeric attribute : "+allElement) #Displays each element into the console
    print("\n")
    for element in nonNumericAttribute: #iterates through the nonNumericAttribute series
        print("String attribute : "+element)  #Displays each element into the console

#Question 3.3 : Avons-nous d'informations sur les dates ?
    print(data.select_dtypes(include='datetime'))


# Question 3.4 : Y a-t-il un attribut vide (NaN)? (utiliser la fonction isnull())
    temp = data.isnull().any() #creates a series that returns true or false based of if there are null values
    if not(temp.all()): #checks if there are 'True'statements in the series temps which signifies that there are null values in the dataframe
        print("Yes, there are some NaN elements") #print yes if there are null values
    

# Question 4.1 : Créer un nouveau dataFrame avec ces attributs.
    dataToStudy = pd.DataFrame(data= data, columns=["CET", "Mean TemperatureC", "Min TemperatureC", "Max TemperatureC", "Mean Humidity", "Max Humidity", "Min Humidity", "MeanDew PointC", "Min DewpointC", "Dew PointC", "CloudCover", "Events"]) 
    #creates a new dataframe  
    

#Question 4.2 : Renommer les attributs pour les rendre plus faciles à manipuler
    dataToStudy.rename(columns = {"CET":"date", "Mean TemperatureC":"Meantemp","Min TemperatureC":"MinTemp","Max TemperatureC":"MaxTemp","Mean Humidity":"MeanHum","Max Humidity":"MaxHum","Min Humidity":"MinHum","MeanDew PointC":"MeanDew","Min DewpointC":"MinDew","Dew PointC":"Dew",}, inplace = True) 
    #Renames the attributes

#calls the differents functions :
    narrowSelection(dataToStudy)  
    cleaningData(dataToStudy)
    dateProcessing(dataToStudy)



main() #runs the "main" method
