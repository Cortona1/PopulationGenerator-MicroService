# Author: Anthony Corton
# Date: 02/11/2021
# Description: This file contains the gui (graphical user interface O_O) for my python population generator
#              microservice. This program will use real data from the census.gov site to retrieve the selected
#              population of a state for its respective year.




import sys



file_list = []
f = open(sys.argv[-1], "r")                # open up the file designated at run time
for line in f:
    file_list.append(line.rstrip())        # append each line of the file to the list till file is read completely
f.close()

#print(file_list) for debugging purposes


if file_list[0] != 'input_year,input_state':

    from tkinter import *
    import requests as req
    from tkinter import ttk
    user_interface = Tk()                # create new Tk object for the user interface

    user_interface.geometry("1300x800")   # set default window size of interface to 1300 width by 800 height
    #user_interface.resizable(width=False, height=False)     # lock window ratio
    user_interface.configure(background='#FFFFC1')


    class Gui:
        """Represents the gui class"""

        def __init__(self, root):
            """The gui class constructor for initializing the variables it takes as a parameter the root"""
            self.frame = Frame(root)
            self.frame.grid()
            self.selected_year = None
            self.selected_state = None
            self.row_counter = 12

        def display_headers(self):
            """Will display the headers of the gui"""

            display_header = Label(user_interface, text="CS-361 Population Generator Microservice ")
            display_creator = Label(user_interface, text="Developed by: Anthony Corton")
            state_header = Label(user_interface,
                                 text="Please select your state of choice from the drop down menu below\nthen "
                                      "choose a corresponding year from the year drop down menu ")

            display_results = Label(user_interface,text="Your results for the search will be shown below:")

            display_header.grid(row=0, column=4, ipady=10)
            #display_header.place(x=600, y=60, anchor="center")

            display_creator.grid(row=1, column=4)
            state_header.grid(row=6, column=0, padx=10, pady=30)
            display_results.grid(row=6,column=8)

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

            state_list.grid(row=8, column=0, ipadx=10)
            year_list.grid(row=8, column=1)

        def create_submit(self):
            """Creates the submit button for clicking a search"""

            submit_button = Button(user_interface, text="Click here to submit state and year query",
                                   command=self.submit_search)

            submit_button_output = Button(user_interface, text="Click here to submit state and year query and output results"
                                                               " to a csv file named output.csv",
                                   command=self.submit_search_output)
            another_sapce = Label(user_interface)
            space = Label(user_interface)
            space.grid(row=10, column=0)
            submit_button.grid(row=11, column=0)
            another_sapce.grid(row=12,column=0)
            submit_button_output.grid(row=13, column=0)

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


        def pop_up_message(self):
            """This function is responsible for showing a pop up message confirming the results of the user's query
            have been successfully written to output.csv"""

            message = Tk()
            message.wm_title("Notification!")
            contents = ttk.Label(message, text="Results have been outputted to output.csv succes"
                                          "sfully")

            contents.pack(side="top", fill="x", pady=10)
            x_button = ttk.Button(message, text="Confirm", command=message.destroy)  # destroy the box when user clicks
            x_button.pack()
            message.mainloop()

        def submit_search(self):
            """Function triggered when user submits a query for state and year"""

            print("You selected the state", self.selected_state.get(), "and the year", self.selected_year.get())

            self.test_api_call()

        def submit_search_output(self):
            """Function triggered when user submits a query for state and year"""

            print("You selected the state", self.selected_state.get(), "and the year", self.selected_year.get())

            retrieved_data = self.test_api_call()
            self.output_file(retrieved_data)
            self.pop_up_message()

        def test_api_call(self):
            """This function is for testing api call"""

            api_url = "https://api.census.gov/data/" + self.selected_year.get() \
                      + "/acs/acs1?get=NAME,B01001_001E&for=state:*"

            response = req.get(api_url)

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
            return population_data

        def output_information(self, data):
            """Takes as a parameter data string and outputs that to the gui as a message box"""
            display_pop = Label(user_interface, text=data)

            display_pop.grid(row=self.row_counter, column=8, padx=10, pady=10)
            self.row_counter+=1


    test_run = Gui(user_interface)

    test_run.display_headers()
    test_run.display_options()
    test_run.create_submit()
    # test_run.test_api_call()
    user_interface.mainloop()


if file_list[0] == 'input_year,input_state':
    import urllib.request        # ZERO CLUE WHY REQUEST WONT WORK FOR THIS BUT WILL FOR GUI I HAVE TO USE URLLIB HAFDHASHDFAS
    import json                  # NEED TO PARSE FOR JSON CONTENT

    def pop_search(year, state):
        """Takes as a parameter a year and a state and will return the population for that search"""

        api_url = "https://api.census.gov/data/" + year + "/acs/acs1?get=NAME,B01001_001E&for=state:*"


        response = urllib.request.urlopen(api_url).read()
        #print(response)

        data = json.loads(response.decode('utf-8'))
        #print(data)
        #pop_data = response.json()
        #print(data)
        # print(response.json())
        population_data = None

        for index in range(1, 53):
            if data[index][0] == state:
                population_data = data[index][1]
                break

        # test = str(self.selected_year.get())
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


        #print(population_date)

    print("There was a input file specified at runtime")
    print("The contents of the input file are the following:", file_list)

    sliced_list = file_list[1:]

    print(sliced_list)

    year = ""
    state = ""
    list_years = []
    list_states = []

    counter = 0

    for row in sliced_list:
        year += row[0] + row[1] + row[2] + row[3]
        list_years.append(year)
        year=""

        comma = 6

        while comma < len(row) - 1:
            state += row[comma]
            comma+=1

        list_states.append(state)
        state=""


    write_file(list_years, list_states)

    print("List of years are the following", list_years)
    print("List of states are the following", list_states)

    write_file(list_years, list_states)
