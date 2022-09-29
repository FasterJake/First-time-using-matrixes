"""Program that obtains the users phone number and zip code.
Then asks the user to enter 18 numbers to fill up 2 3x3 matrices to then
do addition, subtraction, multiplication, or  matrix multiplication on."""


# imports numpy
import numpy as np

# Sets game_answer to false
GAME_ANSWER = False
# While not false while loop continues
while not GAME_ANSWER:
    # Enters loop and asks user if they would like to play
    answer = input("Would you like to play the matrix game, yes or no.\n")
    # If yes continues through loop
    if answer == "yes":

        # Sets is_right to false and begins to do an exception to check input
        IS_RIGHT = False
        # While not false, continues through loop
        while not IS_RIGHT:
            # Asks user to input their phone number, as followed
            phone_number = input("Lets start with your phone number,"
                                 " enter with dashes.(XXX-XXX-XXXX).\n")
            # Exception to check if phonenumber is 12 characters and includes "-"
            if len(phone_number) == 12 and phone_number.__contains__("-"):
                # If statement met, is_right is true
                IS_RIGHT = True
            # If doesn't have required parameters, prints error and goes back to
            # the top of the loop
            else:
                print("Ok we need a phone number, lets get it moving oh wise one.\n")
        # All requirements met exits the loop and prints the users phone number
        print("Nice what a great phone number:" + phone_number + "\n")

        # Prompts user that we are now looking for zip code
        print("Lets get that zipcode now!\n")
        # Sets wrong_zip to false
        WRONG_ZIP = False
        # While not false
        while not WRONG_ZIP:
            # Asks user to enter the zip code to their county or city
            zip_code = input("Please enter the zipcode to your county or city, should be 5 digits.\n")
            # If zip_code is 5 characters, proceed through loop
            if len(zip_code) == 5 and zip_code.isdigit():
                # If statement met, asks user for their 4 digit house number
                house_number = input("Please enter your 4 digit house "
                                 "number to get your full zipcode\n")
                # If house_number is 4 digits, wrong_zip is true
                if len(house_number) == 4 and house_number.isdigit():
                    WRONG_ZIP = True
            # If input does not meet requirement, prints error and goes to top of lp
            else:
                print("Getting there but we need FIVE + FOUR NUMBERS bud. "
                      "Lets redo this form because you ruined it\n")
        # Exits loop, and prints users zipcode and house number
        print("Your zipcode is: " + zip_code + "-" + house_number + "\n")

        # While true
        while True:
            # Try statement to do following
            try:
                # Creates an array
                numpy_list = []
                # sets length_list to 9
                LENGTH_LIST = 9
                # Tells user we are going to work with some matrices and asks for 9 numbers
                print("Ok lets work with some matrices. Please enter 9 numbers.\n")
                # For loop, for i in range of length_list(9)
                # the user will be prompted to enter a number
                for i in range(LENGTH_LIST):
                    # Converts each number to a float and adds them into the numpy_list array
                    numpy_list.append(float(input("Enter that number!\n")))
                # Converts array into a numpy array
                numpy_list = np.array(numpy_list)

                # Creates an array
                numpy_list2 = []
                # sets length_list2 to 9
                LENGTH_LIST2 = 9
                # Asks user to input 9 more numbers for a second numpy array
                print("Please enter 9 more numbers for a second matrix!\n")
                # For loop, for j in range of length_list(9)
                # the user will be prompted to enter a number
                for j in range(LENGTH_LIST2):
                    # Converts each number to a float and adds them into the numpy_list array
                    numpy_list2.append(float(input("Enter that number NOWWW!\n")))
                # Converts array into a numpy array
                numpy_list2 = np.array(numpy_list2)

                # Computes all values in numpy_list into floor values, removing the float
                print(np.floor(numpy_list))
                print("\n")
                # Computes all values in numpy_list into floor values, removing the float
                print(np.floor(numpy_list2))
                print("\n")
                # Reshapes the lists into 3x3 matrices
                print(numpy_list.reshape(3, 3))
                print("\n")
                # Reshapes the lists into 3x3 matrices
                print(numpy_list2.reshape(3, 3))
                print("\n")
                break
            # If numbers are not entered, prints error
            # message and sends back to top of loop
            except ValueError:
                print("Ok buckaroo we need numbers not words,"
                  " eyes on the prize. Lets try this all again.\n")

        # Sets selection to 0
        SELECTION = 0
        # While selection does not = 5
        while SELECTION != 5:
            # Enters loop and starts try statements
            try:
                # Asks user what they would like to do to the matrices
                SELECTION = int(input("What would you like to do to the matrices?\n"
                                "1: Add\n"
                                "2: Subtract\n"
                                "3: Multiply\n"
                                "4: Element to element multiplication\n"
                                "5: To exit.\n"))
                # If selection 1
                if SELECTION == 1:
                    # Adds the 2 matrices together
                    added = numpy_list + numpy_list2
                    # Reshapes the new list into a 3x3 matrix
                    new_add = added.reshape(3, 3)
                    # Prints the original added matrix
                    print("This is the original:\n", new_add)
                    # Transposes the original
                    print("This is the transpose: \n", np.transpose(new_add))
                    # Prints the mean of all the columns
                    added_col_ave = np.mean(new_add, axis=0)
                    print("The average of the columns is:\n", added_col_ave)
                    # Prints the mean of all the rows
                    added_row_ave = np.mean(new_add, axis=1)
                    print("The average of the rows is:\n", added_row_ave)
                    print("\n")

                # If selection is 2
                elif SELECTION == 2:
                    # Subtracts the 2 matrices
                    subtracted = numpy_list - numpy_list2
                    # Reshapes the list into a 3x3 matric
                    new_sub = subtracted.reshape(3, 3)
                    # Prints original
                    print("This is the original:\n", new_sub)
                    # Transposes the original
                    print("This is the transpose: \n", np.transpose(new_sub))
                    # Prints the mean of all the columns
                    subbed_col_ave = np.mean(new_sub, axis=0)
                    print("The average of the columns is:\n", subbed_col_ave)
                    # Prints the mean of all the rows
                    subbed_row_ave = np.mean(new_sub, axis=1)
                    print("The average of the rows is:\n", subbed_row_ave)
                    print("\n")

                # If selection is 3
                elif SELECTION == 3:
                  # Multiplies the matrices together
                    multiplied = numpy_list * numpy_list2
                    # Reshapes the list into a 3x3 matrix
                    new_mult = multiplied.reshape(3, 3)
                    # Prints the original
                    print("This is the original:\n", new_mult)
                    # Transposes the original
                    print("This is the transpose: \n", np.transpose(new_mult))
                    # Prints the mean of all the columns
                    multiplied_col_ave = np.mean(new_mult, axis=0)
                    print("The average of the columns is:\n", multiplied_col_ave)
                    # Prints the mean of all the rows
                    multiplied_row_ave = np.mean(new_mult, axis=1)
                    print("The average of the rows is:\n", multiplied_row_ave)
                    print("\n")
                # If selection is 4
                elif SELECTION == 4:
                    # Uses matmul and reshaping to convert/multiply
                    # each element in the matrices together
                    elements = np.matmul(numpy_list.reshape(3, 3), numpy_list2.reshape(3, 3))
                    # Prints the elements
                    print("Here is the element by element multiplication matrix:\n", elements)
                    print("\n")
                # If selection is 5
                elif SELECTION == 5:
                    # Tells the user goodbye and the program is terminated
                    print("Goodbye good friend. Program terminated.\n")
                    # Tells user that their information
                    # will be sent to their address and phone
                    print("We will be sending all information "
                      "to " + zip_code + "-" + house_number + ". "
                 "We will call at " + phone_number)
                    print("\n")
                    break
            # If numbers were not entered error message is printed and return to top of loop
            except ValueError:
                print("Ok we've been though this, numbers kind friend, use numbers.\n")
    # If answer is no, closes program, and thanks user for participating and to have a good day
    else:
        print("Thank you for using the program and have a nice day!\n")
        break
