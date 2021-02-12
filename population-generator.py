# Author: Anthony Corton
# Date: 02/11/2021
# Description: This file contains the gui (graphical user interface O_O) for my python population generator
#              microservice






from tkinter import *

user_interface = Tk()                # create new gui object for the user interface

user_interface.geometry("1000x800")   # set default window size of interface to 1000 width by 600 height
user_interface.resizable(width=False, height=False)
user_interface.configure(background='#FFFFC1')


display_header = Label(user_interface,text="CS-361 Population Generator Microservice ")
display_creator = Label(user_interface,text="Developed by: Anthony Corton")
state_header = Label(user_interface, text="Please select your state of choice from the drop down menu below\nthen "
                                          "choose a corresponding year from the year drop down menu ")

display_header.grid(row=0, column=6)
display_creator.grid(row=1, column=6)
state_header.grid(row=6, column=0, padx=10, pady= 30)



list_var = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut","Delaware", "Florida",
            "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
            "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
            "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
            "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
            "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]



#  per Sprint 3 Assignment info update "okay to retrieve from just the years that it's available (2005 to 2019) on ACS."
year_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]


year_variable = StringVar(user_interface)
state_variable = StringVar(user_interface)
state_variable.set("New Jersey")               # set default menu selection for state to New Jersey
year_variable.set(2005)


state_list = OptionMenu(user_interface, state_variable, *list_var)
year_list = OptionMenu(user_interface, year_variable, *year_list)

state_list.grid(row=8, column=0)
year_list.grid(row=8, column=1)
user_interface.mainloop()



