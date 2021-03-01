# CS361-MicroService
Course Project


This project is representative of a microservice developed in python that can generator population data from a chosen
state and chosen year. This is real data taken from the census.gov website via an api call. The data has a constraint
for example the microservice will only operate on annual census data ranging from the years 2005-2019 this is by
design per the canvas update on 2/08 -> "For the Sprint 3, you can rely on ACS annual data and it's okay to retrieve
 from just the years that it's available (2005 to 2019) on ACS." - Chanpaisaeng. The next constraint is that the file
 must have input formatted like the following:

input_year,input_state

2015,"New York"

2008,"Oregon"

in a file named input.csv


Next, the output will be formatted like the following in a csv file named output.csv:

input_year,input_state,output_population_size

2015,"New York",19795791

2008,"Oregon",3790060



If the program is run without mentioning a valid file at run time than the gui opens up. There is an option for selecting
a state and a year with two buttons one for showing results on the screen and the other for showing on screen and
outputting to a file named output.csv. There will be a pop up message confirming the file was outputted successfully.

The file must be run with python 3, an example of how to run the program with input.csv in an IDE like PyCharm
would be the following:


population-generator.py input.csv


Imported libraries needed for the program to function:

sys

tkinter

tkk

urllib

json

request

(You will need to install libraries like request with pip if not already installed)

* MicroService communication constraint

The following programs need to be within these folder within the same parent folder for communication to operate

Any Folder

    -> AnthonyC[Pop_Gen_Microservice]  # holds the population-generator.py microservice

    -> DustinF_ContentGenerator        # holds the content-generator.py microservice

    -> JessicaD_PersonGen              # holds the person-generator.py microservice


