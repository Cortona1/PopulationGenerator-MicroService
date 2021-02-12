# Author: Anthony Corton
# Date: 02/11/2021
# Description: This file contains the gui (graphical user interface O_O) for my python population generator
#              microservice




import sys

file_list = []
f = open(sys.argv[-1], "r")                # open up the file designated at run time
for line in f:
    file_list.append(line.rstrip())        # add each line entry to the file list
f.close()

print(file_list)


if file_list[0] != 'input_year,input_state':

    from tkinter import *
    import requests
    user_interface = Tk()                # create new Tk object for the user interface

    user_interface.geometry("1000x800")   # set default window size of interface to 1000 width by 600 height
    user_interface.resizable(width=False, height=False)     # lock window ratio
    user_interface.configure(background='#FFFFC1')


    class Gui:
        """Represents the gui class"""

        def __init__(self, root):
            """The gui class constructor for initializing the variables it takes as a parameter the root"""
            self.frame = Frame(root)
            self.frame.grid()
            self.selected_year = None
            self.selected_state = "Toot"
            self.row_counter = 13

        def display_headers(self):
            """Will display the headers of the gui"""

            display_header = Label(user_interface, text="CS-361 Population Generator Microservice ")
            display_creator = Label(user_interface, text="Developed by: Anthony Corton")
            state_header = Label(user_interface,
                                 text="Please select your state of choice from the drop down menu below\nthen "
                                      "choose a corresponding year from the year drop down menu ")

            display_header.grid(row=0, column=4)
            display_creator.grid(row=1, column=4)
            state_header.grid(row=6, column=0, padx=10, pady=30)

        def display_options(self):
            """Will display the options on the gui for selecting state and year"""

            list_var = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                        "Florida",
                        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
                        "Maine",
                        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                        "Nebraska",
                        "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
                        "Ohio",
                        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
                        "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

            #  per Sprint 3 Assignment info update "okay to retrieve from just the years that it's available (2005 to 2019) on ACS."
            year_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

            year_variable = StringVar(user_interface)
            state_variable = StringVar(user_interface)
            state_variable.set("New Jersey")  # set default menu selection for state to New Jersey
            year_variable.set(2005)


            self.selected_state = state_variable                # assign selected attributed to default ones
            self.selected_year = year_variable


            state_list = OptionMenu(user_interface, state_variable, *list_var)
            year_list = OptionMenu(user_interface, year_variable, *year_list)

            state_list.grid(row=8, column=0)
            year_list.grid(row=8, column=1)

        def create_submit(self):
            """Creates the submit button for clicking a search"""

            submit_button = Button(user_interface, text="Click here to submit state and year query",
                                   command=self.submit_search)

            submit_button_output = Button(user_interface, text="Click here to submit state and year query and output results"
                                                               "to a csv file named output.csv",
                                   command=self.submit_search)

            submit_button.grid(row=10, column=0)
            submit_button_output.grid(row=11, column=0)

        def output_file(self):
            """"""
            var = 10

        def submit_search(self):
            """Function triggered when user submits a query for state and year"""

            print("You selected the state", self.selected_state.get(), "and the year", self.selected_year.get())

            self.test_api_call()

        def test_api_call(self):
            """This function is for testing api call"""

            api_url = "https://api.census.gov/data/" + self.selected_year.get() \
                      + "/acs/acs1?get=NAME,B01001_001E&for=state:*"

            response = requests.get(api_url)

            response.json()
            pop_data = response.json()
            # print(response.json())
            population_data= None

            for index in range(1, 53):
                if pop_data[index][0] == self.selected_state.get():
                    population_data = pop_data[index][1]
                    break

            #test = str(self.selected_year.get())
            data = ("The population for your selected state of " + str(self.selected_state.get()) + " for the year " +
                  self.selected_year.get() + " is " + population_data)

            self.output_information(data)

        def output_information(self, data):
            """Takes as a parameter data string and outputs that to the gui as a message box"""
            display_pop = Label(user_interface, text=data)

            display_pop.grid(row=self.row_counter, column=0, padx=10, pady=10)
            self.row_counter+=1


    test_run = Gui(user_interface)

    test_run.display_headers()
    test_run.display_options()
    test_run.create_submit()
    # test_run.test_api_call()
    user_interface.mainloop()


else:
    print("There was a input file specified at runtime")
    print("The contents of the input file are the following:", file_list)





