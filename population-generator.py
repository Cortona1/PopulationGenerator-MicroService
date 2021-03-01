# Author: Anthony Corton
# Date: 02/11/2021
# Description: This file contains the gui (graphical user interface O_O) for my python population generator
#              microservice. This program will use real data from the census.gov site to retrieve the selected
#              population of a state for its respective year.


import sys

file_list = []
f = open(sys.argv[-1], "r")                     # open up the file designated at run time
for line in f:
    file_list.append(line.rstrip())
f.close()

if file_list[0] != 'input_year,input_state':

    from tkinter import *
    import requests as req
    from tkinter import ttk
    user_interface = Tk()

    user_interface.geometry("1400x800")         # keep resizing window available
    user_interface.configure(background='#FFFFC1')

    from os import listdir
    from os.path import isfile, join
    import os

    class Gui:
        """Represents the gui class for the population generator microservice"""

        def __init__(self, root):
            """The gui class constructor for initializing the variables it takes as a parameter the root of the
            Tk object created"""
            self.frame = Frame(root)
            self.frame.grid()
            self.selected_year = None
            self.selected_state = None
            self.row_counter = 8

            self.plain_text = StringVar()
            self.display_output = Label(user_interface, textvariable=self.plain_text)
            self.display_output.grid(row=self.row_counter, column=8, padx=10, pady=10)

        def display_headers(self):
            """Will display the headers of the gui"""

            display_header = Label(user_interface, text="CS-361 Population Generator Microservice ")
            display_creator = Label(user_interface, text="Developed by: Anthony Corton")
            state_header = Label(user_interface,
                                 text="Please select your state of choice from the drop down menu below\nthen "
                                      "choose a corresponding year from the year drop down menu ")

            display_results = Label(user_interface,text="Your results for the search will be shown below:")

            display_header.grid(row=0, column=4, ipady=10)
            display_creator.grid(row=1, column=4)
            state_header.grid(row=6, column=0, padx=10, pady=30)
            display_results.grid(row=6,column=8)

        def create_display_list(self):
            """Creates the list of options that will be displayed to the gui as a list of available states and
            years and will return the list"""

            state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                          "Delaware","Florida",
                        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
                        "Maine",
                        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                        "Nebraska",
                        "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
                        "North Dakota",
                        "Ohio",
                        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
                        "Tennessee",
                        "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

            #  per Sprint 3 Assignment update "okay to retrieve years 2005 to 2019 on ACS."
            year_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

            return [state_list, year_list]

        def display_options(self):
            """Will display the options on the gui for selecting state and year"""
            options_list = self.create_display_list()

            year_variable = StringVar(user_interface)
            state_variable = StringVar(user_interface)
            state_variable.set("New Jersey")                    # set default menu selection to New Jersey 2005
            year_variable.set(2005)

            self.selected_state = state_variable
            self.selected_year = year_variable

            state_menu = OptionMenu(user_interface, state_variable, *options_list[0])
            year_menu = OptionMenu(user_interface, year_variable, *options_list[1])

            state_menu.grid(row=8, column=0, ipadx=10)
            year_menu.grid(row=8, column=1)

        def read_content_output(self):
            """Handles searching for the data from the content generator microservice which is formatted as
            content_output.csv, will print to console contents if file is found or an error message if not"""

            directory_files = [file for file in listdir(sys.path[0]) if isfile(join(sys.path[0], file))]
            file_importance = "content_output.csv"

            if file_importance not in directory_files:
                print("File not found, please click check for request from population generator microservice in the"
                      " content generator microservice")

            else:
                self.display_content_output()

        def display_content_output(self):
            """Handles displaying the contents of content_output.csv to the console via print statements"""

            reference_list = []
            with open("content_output.csv", "r") as file:
                for entry_list in file:
                    reference_list.append(entry_list.strip())

            print(reference_list)

            print("Headers")
            print(reference_list[0] + "\n")

            for index in range(len(reference_list)):
                if index != 0:
                    print(reference_list[index])

        def check_request(self):
            """Will check for request from person generator microservice and if there is a request will output data
            in a file named population_output.csv so that the person generator service can locate and read it"""

            directory_files = [file for file in listdir(sys.path[0]) if isfile(join(sys.path[0], file))]
            file_importance = "population_request.csv"

            if file_importance not in directory_files:
                print("File not found, please make sure a request for input was sent from"
                      " the person generator microservice as 'population_request.csv' "
                      " button must be pressed manually to search again")

            else:
                self.submit_revised_output()
                self.pop_up_message("Data has been outputted to population_output.csv, please check the"
                                    "check for input request in person_generator")

        def create_check_button(self):
            """Handles creating the check for request button button"""
            check_button = Button(user_interface, text="Click here to check for request from person_generator "
                                                         "microservice", command=self.check_request)
            space = Label(user_interface)

            space.grid(row=20, column=0)
            check_button.grid(row=21, column=0)

        def request_content(self):
            """Handles writing the request file to the content generator microservice"""

            original_file_path = os.getcwd()
            path_parent = os.path.dirname(os.getcwd())

            person_gen_path = path_parent + "\DustinF_ContentGenerator"
            os.chdir(person_gen_path)

            with open("content_request.csv", "w") as file:
                file.write("This is a request for content from population generator microservice to content"
                           "generator microservice")

            os.chdir(original_file_path)

        def create_request_button(self):
            """Creates the request button for requesting information from the content generator microservice"""

            request_button = Button(user_interface, text="Click here to request input from content generator "
                                                         "microservice", command=self.request_content)

            check_button = Button(user_interface, text="Check for content_output.csv", command=self.read_content_output)
            space = Label(user_interface)

            space.grid(row=18,column=0)
            request_button.grid(row=19,column=0)
            check_button.grid(row=19,column=1)

        def create_submit(self):
            """Creates the submit button for clicking a search of state and year"""

            submit = Button(user_interface, text="Click here to submit state and year query",
                                   command=self.submit_search)

            submit_output = Button(user_interface, text="Click here to submit state and year query and output results"
                                                               " to a csv file named output.csv",
                                   command=self.submit_search_output)

            another_space = Label(user_interface)
            space = Label(user_interface)
            space.grid(row=10, column=0)
            submit.grid(row=11, column=0)
            another_space.grid(row=12,column=0)
            submit_output.grid(row=13, column=0)

        def output_file(self, population_data):
            """Receives as a parameter population data from the test api call function and writes to output.csv that
            information in the recognized format specified in the assignment instructions."""
            with open("output.csv", "w") as file:
                file.write("input_year,input_state,output_population_size\n")

                file.write(str(self.selected_year.get()))
                file.write(',"')
                file.write(str(self.selected_state.get()))
                file.write('",')
                file.write(str(population_data))
                file.write("\n")

        def output_file_communication(self, population_data):
            """Receives as a parameter population data from the test api call function and writes to output.csv that
            information in the recognized format specified in the assignment instructions."""

            original_file_path = os.getcwd()                    
            path_parent = os.path.dirname(os.getcwd())

            person_gen_path = path_parent + "\JessicaD_PersonGen"
            os.chdir(person_gen_path)

            with open("population_output.csv", "w") as file:
                file.write("input_year,input_state,output_population_size\n")
                file.write(str(self.selected_year.get()))
                file.write(',"')
                file.write(str(self.selected_state.get()))
                file.write('",')
                file.write(str(population_data))
                file.write("\n")
            
            os.chdir(original_file_path)

        def pop_up_message(self, text):
            """This function is responsible for showing a pop up message confirming the results of the user's query
            have been successfully written to output.csv"""

            message = Tk()
            message.wm_title("Notification!")
            contents = ttk.Label(message, text=text)

            contents.pack(side="top", fill="x", pady=10)
            x_button = ttk.Button(message, text="Confirm", command=message.destroy)
            x_button.pack()
            message.mainloop()

        def submit_search(self):
            """Function triggered when user submits a query for state and year"""

            self.test_api_call()

        def submit_search_output(self):
            """Function triggered when user submits a query for state and year"""

            retrieved_data = self.test_api_call()
            self.output_file(retrieved_data)
            self.pop_up_message("Results have been outputted to output.csv successfully")

        def submit_revised_output(self):
            """Function triggered when user submits a query for state and year"""

            retrieved_data = self.test_api_call()
            self.output_file_communication(retrieved_data)
            self.pop_up_message("Results have been outputted to population_output.csv successfully")

        def test_api_call(self):
            """This function is for testing api call"""

            api_url = "https://api.census.gov/data/" + self.selected_year.get() \
                      + "/acs/acs1?get=NAME,B01001_001E&for=state:*"

            response = req.get(api_url)

            response.json()
            pop_data = response.json()
            population_data= None

            for index in range(1, 53):
                if pop_data[index][0] == self.selected_state.get():
                    population_data = pop_data[index][1]
                    break

            data = ("The population for your selected state of " + str(self.selected_state.get()) + " for the year " +
                  self.selected_year.get() + " is " + population_data)

            self.output_information(data)
            return population_data

        def output_information(self, data):
            """Takes as a parameter data string and outputs that to the gui as a message box"""

            self.plain_text.set(data)


    test_run = Gui(user_interface)
    test_run.display_headers()
    test_run.display_options()
    test_run.create_submit()
    test_run.create_request_button()
    test_run.create_check_button()
    user_interface.mainloop()


if file_list[0] == 'input_year,input_state':
    import urllib.request
    import json

    def pop_search(year, state):
        """Takes as a parameter a year and a state and will return the population for that search"""

        api_url = "https://api.census.gov/data/" + year + "/acs/acs1?get=NAME,B01001_001E&for=state:*"

        response = urllib.request.urlopen(api_url).read()

        data = json.loads(response.decode('utf-8'))
        population_data = None

        for index in range(1, 53):
            if data[index][0] == state:
                population_data = data[index][1]
                break

        return population_data

    def write_file(list_years, list_states):
        """Takes a list of years and states and will output the population for those states and their respective years
        to a file called output.csv"""

        population_date = []

        for x in range(len(list_states)):
            pop_results = pop_search(list_years[x], list_states[x])
            population_date.append(pop_results)

        with open("output.csv", "w") as file:
            file.write("input_year,input_state,output_population_size\n")
            for data in range(len(population_date)):
                file.write(str(list_years[data]))
                file.write(',"')
                file.write(list_states[data])
                file.write('",')
                file.write(str(population_date[data]))
                file.write("\n")


    print("There was a input file specified at runtime")
    print("The contents of the input file are the following:", file_list)

    sliced_list = file_list[1:]

    year = ""
    state = ""
    list_years = []
    list_states = []

    counter = 0

    for row in sliced_list:
        year += row[0] + row[1] + row[2] + row[3]
        list_years.append(year)
        year = ""

        comma = 6

        while comma < len(row) - 1:
            state += row[comma]
            comma += 1

        list_states.append(state)
        state = ""

    write_file(list_years, list_states)

    print("List of years are the following", list_years)
    print("List of states are the following", list_states)

    write_file(list_years, list_states)
