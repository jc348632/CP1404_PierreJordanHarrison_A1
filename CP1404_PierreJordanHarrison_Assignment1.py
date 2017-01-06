"""
Pierre Jordan Harrison
6 January 2017
The program is to load a list of items from a csv file, then the user can choose to list the items, hire the items, return the items, or add another items
The program ended with saving the current situation of all the items into the csv file
Github link:
"""
from operator import itemgetter
FILENAME = "books.csv"
file_list = []

def header(): #this function is to shows the number of books contain in books.csv
    print("Reading List 1.0 - by Pierre Jordan Harrison \n{} books loaded from books.csv".format(len(file_list)))

def mainMenu():
    """To show main menu and ask for input, then return it afterwards"""
    print("Menu \nR - List required books \nC - List completed books \nA - Add new book \nM - Mark a book as completed \nQ - Quit")#Print the main menu
    menuSelection = input(">>>")#Asking for menu input
    menuSelection = menuSelection.upper()#Making the input into capital letters
    return menuSelection #Return the menu input

def main():
    """Start of the program welcoming the user"""
    read_file()#to call function read_file()
    header()#to call function header to show
    menuSelection = mainMenu()#to connected between menuSelection and mainMenu()
    while menuSelection: #While menuSelection is True (This is while loop [Infinity Loop]), this also function to checks whether the option given by the user is valid or not
        if menuSelection == "R": #If user enter R, this will go to req_books() function
            req_books()
        elif menuSelection == "C": #If user enter C, this will go to comp_books() funciton
            comp_books()
        elif menuSelection == "A": #If user enter A, this will go to add_books() funciton
            add_books()
        elif menuSelection == "M":#If user enter M, this will go to marked_books() funciton
            marked_books()
        elif menuSelection == "Q":#If user enter Q, this will go to q_program() funciton
            q_program()
            break #to finish the loop
        else:
            print("Invalid Menu Choice") #If user enter out of R, C, A, M, Q will be shown "Invalid Menu Choice"
            menuSelection = mainMenu()
    print("{} books saved to {}".format(len(file_list), FILENAME)) #print the number of books in file_list which saved to FILENAME
    print("Have a nice day :)")#Print string "Have a nice day :)"

def req_books():
    """function to show the user the required books to read."""
    total_pages = 0#to declare the variable
    count_completed = 0#start form 0
    print("Required books:")#print Required books
    for index, e in enumerate(file_list):#to show index is the number to list the books and e is the first order books in file_list
        if e[3] == "r":#if the third part in books.csv is "r" print ("{} {:40s} by {:20s} {} pages".format(index, e[0], e[1], e[2]))
            print("{} {:40s} by {:20s} {} pages".format(index, e[0], e[1], e[2]))
            total_pages += int(e[2])#total_pages depends in the second part of books.csv
                                    #for example: (0)Developing the Leader Within You,(1)John Maxwell,(2)225,(3)r
                                    # the second part is "225", third part is "r"
            count_completed += 1
    if count_completed == 0:#print No book required yet if none to required / 0
        print("No book required yet")
    else:#if books still required print ("Total pages for {} book(s): {} pages \n".format(count_completed, total_pages))
        print("Total pages for {} book(s): {} pages \n".format(count_completed, total_pages))
    #This function :return: none

def comp_books():
    """function to show the user the completed books."""
    total_pages = 0 #declare variable
    count_completed = 0 #declare a variable to count the amount of completed books
    print("Completed books:") #print "Completed books:"
    for index, e in enumerate(file_list):#to show index is the number to list the books and e is the first order books in file_list
        if e[3] == "c":#if the third part in books.csv is "c" print ("{} {:40s} by {:20s} {} pages".format(index, e[0], e[1], e[2]))
            print("{} {:40s} by {:20s} {} pages".format(index, e[0],e[1],e[2]))
            total_pages += int(e[2])#total_pages depends in the second part of books.csv
                                    #for example: (0)Developing the Leader Within You,(1)John Maxwell,(2)225,(3)r
                                    # the second part is "225", third part is "r"
            count_completed += 1
    if count_completed == 0:#print No book completed yet if none to required / 0
        print("No book completed yet")
    else:#if books have completed print ("Total pages for {} book(s): {} pages \n".format(count_completed, total_pages))
        print("Total pages for {} book(s): {} pages \n".format(count_completed,total_pages))
    #This function :return: none

def add_books(): #This function is to add more books to books.csv
    """
    add_new_book = []#for user to input books
    while True:#using while loops
        title_name = str(input("Title: "))#input the title
        if len(title_name) <1:#if the title blank it will shown "Input can not be blank"
            print("Input can not be blank")
        else:
            break #to end the loop
    add_new_book.append(title_name) #add to the list add_new_book from the title_name
    while True:
        author_name = str(input("Author: ")) #input the Author
        if len(author_name) < 1: #if the author blank it will shown "Input can not be blank"
            print("Input can not be blank")
        else:
            break #to end the loop
    add_new_book.append(author_name) #add to the list add_new_book from the author_name
    while True: #while loop
        try:
            number_of_pages = int(input("Pages: ")) # to input hte number of pages
            if number_of_pages <= 0: # the number of pages should >= 0 if not it will be printed "Pages must be >=0"
                print("Pages must be >=0")
            else:
                break #to end the loop
        except ValueError: #to avoid value error like words or symbols (pages must be in numbers)
            print("Invalid input; enter a valid number")
    add_new_book.append(str(number_of_pages))
    add_new_book.append("r") #add a 'r' code to detected as required book
    print(add_new_book)
    file_list.append(add_new_book)
    file_list.sort(key=itemgetter(1, 2))
    """
    add_new_book = []#for user to input books
    while True:#using while loops
        title_name = str(input("Title: "))#input the title
        if len(title_name) <1:#if the title blank it will shown "Input can not be blank"
            print("Input can not be blank")
        else:
            break #to end the loop
    add_new_book.append(title_name) #add to the list add_new_book from the title_name
    while True:
        author_name = str(input("Author: ")) #input the Author
        if len(author_name) < 1: #if the author blank it will shown "Input can not be blank"
            print("Input can not be blank")
        else:
            break #to end the loop
    add_new_book.append(author_name) #add to the list add_new_book from the author_name
    while True: #while loop
        try:
            number_of_pages = int(input("Pages: ")) # to input hte number of pages
            if number_of_pages <= 0: # the number of pages should >= 0 if not it will be printed "Pages must be >=0"
                print("Pages must be >=0")
            else:
                break #to end the loop
        except ValueError: #to avoid value error like words or symbols (pages must be in numbers)
            print("Invalid input; enter a valid number")
    add_new_book.append(str(number_of_pages))
    add_new_book.append("r") #add a 'r' code to detected as required book
    print(add_new_book)
    file_list.append(add_new_book)
    file_list.sort(key=itemgetter(1, 2))


def marked_books():#A function to mark a book as complete
    """
    req_books() #call function req_books()
    count = 0 #to declare the variable
    for each in file_list: # for loop
        if each[3] == "r":
            count += 1
    if count == 0:
        pass
    else:
        print("Enter the number of a book to mark as completed ")
        while True:#while loops
            try:
                mark_complete = int(input(">>>")) #for user to input which books wanted to marked as complete
                break #end the loop
            except ValueError: #to avoid any value error like words and symbols (book code must be in numbers)
                print("Invalid input; enter a valid number")
        for index, each in enumerate(file_list):
            if index == mark_complete:
                if each[3] == "r": #to check wheter the book has already marked as complete / not
                    each[3] = "c" #changing the code from file_list to be marked as completed (c)
                    print("{} by {} marked as completed".format(each[0],each[1]))
                else:
                    print("That book is already completed")
                print("")
        # This function :return: none
    """
    req_books() #call function req_books()
    count = 0 #to declare the variable
    for each in file_list: # for loop
        if each[3] == "r":
            count += 1
    if count == 0:
        pass
    else:
        print("Enter the number of a book to mark as completed ")
        while True:#while loops
            try:
                mark_complete = int(input(">>>")) #for user to input which books wanted to marked as complete
                break #end the loop
            except ValueError: #to avoid any value error like words and symbols (book code must be in numbers)
                print("Invalid input; enter a valid number")
        for index, each in enumerate(file_list):
            if index == mark_complete:
                if each[3] == "r": #to check wheter the book has already marked as complete / not
                    each[3] = "c" #changing the code from file_list to be marked as completed (c)
                    print("{} by {} marked as completed".format(each[0],each[1]))
                else:
                    print("That book is already completed")
                print("")
        # This function :return: none

def read_file():
    """this function to call file from books.csv"""
    global file_list #to make it global
    file_pointer= open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()#to strip the data
        datum = data.split(",") #to split the data to the datum list
        file_list.append(datum)#to save all the datum in file_list. inside file_list is the datum (list)
    file_list.sort(key=itemgetter(1, 2))
    file_pointer.close() #to close
    return file_list #return file_list

def q_program():
    """To write the current data into the file"""
    output_file = open(FILENAME, "w") #To open the file for writing, thus overwrite the previous data
    for each in file_list: #To iterate through the data
        books = "{},{},{},{}".format(each[0],each[1],each[2],each[3]) + "\n" #To re-arrange the data
        output_file.write(books) #write the arranged data into the books.csv
    output_file.close() #close the file

main()