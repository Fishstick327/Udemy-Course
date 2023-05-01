import os

file_path = r'C:\Users\natha\Desktop\WEd Development  bootcamp\Udemy Code\new_prj\weather_data.csv'
#or alternatively 
file_path_alternative = os.path.join(os.path.dirname(__file__), "file_name")

#readline() reads the first line of the file and returns a string
""" with open(file_path, mode="r") as data_file:
    data = data_file.readline()
    print(data) """
    
#readline"s"() reads all the lines of the file and returns a list
""" with open(file_path, mode="r") as data_file:
    data = data_file.readlines()
    print(data) """
    
#read() reads the whole file as is

#reader() a method from the csv module that reads the file and returns a list of lists
    #this return a list of individual rows with individual string that can be call for
import csv
""" with open(file_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp": #remove the label "temp"
            temperatures.append(int(row[1])) #convert the string to int
    print(temperatures) """
    
import pandas #a python data analysis, data manipulation and data cleaning tool
data = pandas.read_csv(file_path)
print(data['temp'])

    
"""
int() will not work in pandas because they use their own data type
    #instead we use iloc[] to get the data that is a int value from the csv file
-iloc() is use for integer base indexing to select row and column by their integer position
    -example, df.iloc[0:5, 2] would return the first five rows of the third column of the DataFrame df.
    -iloc() is for multiple rows and columns

-iat() use for fast scalar access of a DataFrame to a "single" value, similar to iloc but only return
    a single value and is faster than iloc(). Ex: df.iat[0, 2] access the first row and third column
    
    
    
    
    
"""