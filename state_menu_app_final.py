"""Vanessa Abrahams
This application will providing users with the
ability to search and display U.S. State Capital, population and Flowers."""

import sys
import matplotlib.pyplot as plt
from PIL import Image

# states list holds the US state information
states = [['Alabama', 'Montgomery', 4887680, 'Camellia'],
          ['Alaska', 'Juneau', 735139, 'Forget-Me-Not'],
          ['Arizona', 'Phoenix', 7158020, 'Saguaro Cactus Blossom'],
          ['Arkansas', 'Little Rock', 3009730, 'Apple Blossom'],
          ['California', 'Sacramento ', 39461600, 'California Poppy'],
          ['Colorado', 'Denver', 5691290, 'White and Lavender Columbine'],
          ['Connecticut', 'Hartford', 3571520, 'Mountain Laurel'],
          ['Delaware', 'Dover', 965479, 'Peach Blossom'],
          ['Florida', 'Tallahassee', 21244300, 'Orange Blossom'],
          ['Georgia', 'Atlanta', 10511100, 'Cherokee Rose'],
          ['Hawaii', 'Honolulu', 1420590, 'Hibiscus'],
          ['Idaho', 'Boise', 1750540, 'Syringa'],
          ['Illinois', 'Springfield', 12723100, 'Purple Violet'],
          ['Indiana', 'Indianapolis', 6695500, 'Peony'],
          ['Iowa', 'Des Moines', 3148620, 'Wild Prairie Rose'],
          ['Kansas', 'Topeka', 2911360, 'Sunflower'],
          ['Kentucky', 'Frankfort', 4461150, 'Goldenrod'],
          ['Louisiana', 'Baton Rouge', 4659690, 'Magnolia'],
          ['Maine', 'Augusta', 1339060, 'White Pine Cone & Tassel'],
          ['Maryland', 'Annapolis', 6035800, 'Black-Eyed Susan'],
          ['Massachusetts', 'Boston', 6882640, 'Mayflower'],
          ['Michigan', 'Lansing', 9984070, 'Apple Blossom'],
          ['Minnesota', 'St.Paul', 5606250, 'Pink and White Lady Slipper'],
          ['Mississippi', 'Jackson', 2981020, 'Magnolia'],
          ['Missouri', 'Jefferson City', 6121620, 'White Hawthorn Blossom'],
          ['Montana', 'Helena', 1060660, 'Bitterroot'],
          ['Nebraska', 'Lincoln', 1925610, 'Goldenrod'],
          ['Nevada', 'Carson City', 3027340, 'Sagebrush'],
          ['New Hampshire', 'Concord', 1353460, 'Purple Lilac'],
          ['New Jersey', 'Trenton', 8886020, 'Violet'],
          ['New Mexico', 'Santa Fe', 2092740, 'Yucca Flower'],
          ['New York', 'Albany', 19530400, 'Rose'],
          ['North Carolina', 'Raleigh', 10381600, 'Dogwood'],
          ['North Dakota', 'Bismarck', 758080, 'Wild Prairie Rose'],
          ['Ohio', 'Columbus', 11676300, 'Scarlet Carnation'],
          ['Oklahoma', 'Oklahoma City', 3940240, 'Mistletoe'],
          ['Oregon', 'Salem', 4181890, 'Oregon Grape'],
          ['Pennsylvania', 'Harrisburg', 12800900, 'Mountain Laurel'],
          ['Rhode Island', 'Providence', 1058290, 'Violet'],
          ['South Carolina', 'Columbia', 5084160, 'Yellow Jessamine'],
          ['South Dakota', 'Pierre', 878698, 'Pasque Flower'],
          ['Tennessee', 'Nashville', 6771630, 'Iris'],
          ['Texas', 'Austin', 28628700, 'Bluebonnet'],
          ['Utah', 'Salt Lake City', 3153550, 'Sego Lily'],
          ['Vermont', 'Montpelier', 624358, 'Red Clover'],
          ['Virginia', 'Richmond', 8501290, 'Dogwood'],
          ['Washington', 'Olympia', 7523870, 'Pink Rhododendron'],
          ['West Virginia', 'Charleston', 1804290, 'Rhododendron'],
          ['Wisconsin', 'Madison', 5807410, 'Wood Violet'],
          ['Wyoming', 'Cheyenne', 577601, 'Indian Paintbrush']]


def order_states():
    """Sorts and prints states in alphabetical order"""
    print("*** See list of US States below ***")
    for i, state in enumerate(states):
        # sort states into alphabetical order and then print
        sorted(states)
        print("State: ", states[i][0], "\n", "Capital: ", states[i][1], "\n", "Population: ", states[i][2], "\n",
              "Flower: ", states[i][3], "\n", )


def state_info():
    """"Searches for a state, then prints state information and state flower image"""
    print("What state would you like to search?")
    # state_lookup to hold user input
    while True:
        try:
            state_lookup = input()
            # iterate over the states list and find the input value
            for i, state in enumerate(states):
                # if the input matches what's on the list, print state info
                if state_lookup == (states[i][0]):
                    print("You entered: \n", 'State: ', states[i][0], '    Capital: ', states[i][1],
                          '    Population: ', states[i][2], '    Flower: ', states[i][3])
                    # locate stored image
                    image = Image.open(state_lookup.lower() + '.jpg')
                    # show stored image
                    image.show()
        except ValueError:
            for i, state in enumerate(states):
                # else if the input doesn't match what's in the array, return to menu
                if i > 51:
                    print("")
        break


def top_5_states():
    """Prints bar graph of the top 5 most populous states"""
    # store values in x and y axis
    x_axis = [states[4][0], states[42][0], states[8][0], states[31][0], states[37][0]]
    y_axis = [states[4][2], states[42][2], states[8][2], states[31][2], states[37][2]]

    plt.bar(x_axis, y_axis)
    # set properties for the bar graph
    plt.title('Top 5 Most Populous States')
    plt.xlabel('State')
    plt.ylabel('Population')
    plt.xticks([1, 2, 3, 4, 5])
    plt.yticks([])
    plt.show()


def population_update():
    """Updates the overall population for a specific state"""
    while True:
        try:
            state_input = input("What is the state you wish to update? ")
            population = int(input("What is " + state_input + "'s new population? "))
            for i, state in enumerate(states):
                # if state input matches state name in the array, change population value and print
                if state_input == (states[i][0]):
                    states[i][2] = population
                    print(states[i][:4])
                    print("*****See the new population for ", state_input, " in the list below. *****")
                    for i in range(len(states)):
                        print(states[i][0], "\n", states[i][1], "\n", states[i][2], "\n", states[i][3], "\n",)
        except ValueError:
            for i, state in enumerate(states):
                # if there is no match, reprint question asking about the
                # state and population to be updated
                if i > 51:
                    print("")
        # return to the main menu
        break


MENU_ENTRY = 1
# begin while statement to continue through out the program until user quits
while True:
    print("Welcome to the U.S. States application. Here are the menu options:")
    print("1. Display all US States in Alphabetical order\n"
          "2. Search for a state and display the appropriate "
          "Capital name, state population, and associate State flower image\n"
          "3. Bar graph of the top 5 populated States and overall population\n"
          "4. Update the overall state population for a state\n"
          "5. Exit Program")
    try:
        MENU_ENTRY = int(input("Enter your menu selection: "))
        # set up menu for different options, including the functions to run
        if MENU_ENTRY == 1:
            order_states()

        elif MENU_ENTRY == 2:
            state_info()

        elif MENU_ENTRY == 3:
            top_5_states()

        elif MENU_ENTRY == 4:
            population_update()

        elif MENU_ENTRY == 5:
            print("Thank you for visiting. Good day.")
            sys.exit()
        # if user input isn't one of the allowable inputs, will reprint menu options
        elif MENU_ENTRY >= 6:
            print('Please only enter a value between 1 and 5')
    # if user input isn't one of the allowable inputs, will reprint menu options
    except ValueError:
        if MENU_ENTRY != int:
            print("Invalid entry. You must enter an integer between 1 and 5")
