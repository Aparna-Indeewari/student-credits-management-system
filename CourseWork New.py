# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 18672064
# Date: 06.12.2021


#Global variables for counters in histogram
prog_count = 0
mod_ret_count = 0
mod_tra_count = 0
exclude_count = 0
total_count = 0
progression = []


def validatingInput(pCreditType):
    '''Prompting credits from user, validating them and
        return credits'''

    while (True):
        try:
            credits = int(input(f'\nPlease enter your {pCreditType}: '))
            if credits in range (0, 121, 20):
                break
            
            else:
                print ('Out of range')

        except ValueError :             # Exception Handling for ValueError
            print ('Integer Required')

    return credits



def displayingOutcome (pPass, pDiffer, pFail):

    '''Categorizing Student progression outcomes according to parameters pPass, pDiffer and pFail
        and displaying them.
        Counting the number of outcomes for each category.
        Appending each user input to the progression list.'''

    global prog_count, mod_ret_count, mod_tra_count, exclude_count, total_count

    if pPass == 120 :
        print ('\nProgress')
        prog_count += 1
        progression.append(f'Progress - {pPass} , {pDiffer}, {pFail}') #Appending the user inputs to the progression list as a string
        
    elif pPass == 100:
        print ('\nProgress (module trailer)')
        mod_tra_count += 1
        progression.append(f'Progress (Module Trailer) - {pPass} , {pDiffer}, {pFail}')  #Appending the user inputs to the progression list as a string
    
    elif pFail >= 80:
        print ('\nExclude')
        exclude_count += 1
        progression.append(f'Module Retreiver - {pPass} , {pDiffer}, {pFail}')   #Appending the user inputs to the progression list as a string

    else:
        print ('\nModule Retriever')
        mod_ret_count += 1
        progression.append(f'Exclude - {pPass} , {pDiffer}, {pFail}')   #Appending the user inputs to the progression list as a string

    total_count += 1 #Counting the number of inputs



def studentVersion():
    '''Calling the ValidatingInput function and checking the total of returned values are equal to 120
        Calling the displayingOutcome function'''
    while(True):

        credits_at_pass = validatingInput ('Credits at pass')
        credits_at_defer = validatingInput ('Credits at defer')
        credits_at_fail = validatingInput ('Credits at fail')

        #Checking weather the total of credits is within the range
        if (credits_at_pass + credits_at_defer + credits_at_fail != 120):
            print('\nTotal Incorrect!! Enter your credits again')
            
        else:
            break

    displayingOutcome (credits_at_pass,credits_at_defer, credits_at_fail)



def horizontalHistogram():
    '''Displaying Student's Progression Outcome as a Horizontal Histogram'''

    print('\n__________________________________________________________________________________________________________________')
    print ('Horizontal Histogram\n')
 
    print (f"Progress {prog_count:2} {':':>5}  {'*'*prog_count}" )
    print (f"Trailer {mod_tra_count:2} {':':>6}  {'*'*mod_tra_count}" )
    print (f"Retreiver {mod_ret_count:2} {':':>4}  {'*'*mod_ret_count}" )
    print (f"Exclude {exclude_count:2} {':':>6}  {'*'*exclude_count}" )
    
    print (f'\n{total_count} outcomes in total.')
    print ('____________________________________________________________________________________________________________________')
            


def staffVersion():
    '''Looping the student version function allowing the user to enter more than one student's progress'''
    
    user_input = 'y'
    while (True):

        if user_input == 'y':
            studentVersion()
            print ('\nWould you like to continue?')
            user_input = (input ("Press 'y' to continue or press 'q' to quit: ")).lower()

        elif user_input == 'q':
            horizontalHistogram()                      # Displaying Horizontal Histogram
            break 

        elif user_input != 'y' and user_input != 'q' :
            print ('\nInvalid Selection !! ')           #If user input is not y or q
            user_input = (input ("Press 'y' to continue or press 'q' to quit: ")).lower()



def verticalHistogram():
    '''Displaying Student's Progression Outcome as a Vertical Histogram'''

    print('\nVertical Histogram\n')
    header = [ f'Progress {prog_count} |', f'Trailer {mod_tra_count} |', f'Retriever {mod_ret_count} |', f'Excluded {exclude_count} |']  # Creating a list fot the header of the vertical histogram 
    print (' '.join(header))

    for x in range (max(prog_count, mod_ret_count, mod_tra_count, exclude_count)):  
        if x < prog_count:
            print (f"{'*':>5}", end = '')
        else:
            print (f"{' ':>5}", end = '')
        
        if x < mod_tra_count:
            print (f"{'*':>12}", end = '')
        else:
            print (f"{' ':>12}", end = '')
       
        if x < mod_ret_count:
            print (f"{'*':>13}", end = '')
        else:
            print (f"{' ':>13}", end = '')
              
        if x < exclude_count:
            print (f"{'*':>13}")
        else:
            print (f"{' ':>13}")

    print (f'\n{total_count} outcomes in total.')
    
  
def DisplayingList (pProgression):
    '''Displaying the progression outcome stored in the list '''

    for items in pProgression:
        print (items)


def writingFile (pProgression):
    '''Writing the progression outcome stored in the list, to a file'''

    print('\n\nYour Progression Outcome will be saved in the Progression.txt File\n')
    with open ('Progression.txt', 'w') as prog_file:
        for items in pProgression:
            prog_file.write(str(f' {items} \n'))
     
    print ('File Writing is Successful\n')


def ReadFile ():
    '''Read the Progression.txt file'''

    with open ('Progression.txt', 'r') as r_prog_file:
        for line in r_prog_file:
            print (line, end = '')
        









#main Code
print ('                                        ****Student Progression Outcomes**** \n\n')

#Displaying the menu with 4 options and asking the user to prompt the option with the keyboard
print ('Choose the part you want to continue from below menu')

print ('\n1> Student Version and Staff Version with Horizontal Histogram')
print ('2> Extended Staff Version with Vertical Histogram')
print ('3> Extended Staff Version with List')
print ('4> Extended Staff Version with the Txt File\n')


while (True):
    try:
        menu_selection = int(input('Enter your selection here: '))

        #Student Version and Staff Version with Horizontal Histogram
        if menu_selection == 1:
            print('\n1> Enter 1 for Student Version')
            print('2> Enter 2 for Staff Version')

            while (True):
                choice = int(input('\nEnter your selection here: ')) #Asking user from prompt whether to use student version or Staff version

                if choice == 1:
                    studentVersion()
                    break

                elif choice == 2:
                    staffVersion()
                    break

                else:
                    print ('Invalid Selection!! Try again using ONLY 1 and 2 \n') # If user enters an invalid input

            break

        elif menu_selection == 2:
            staffVersion()
            verticalHistogram()
            break

        elif menu_selection == 3:
            staffVersion()
            verticalHistogram()
            print ()
            DisplayingList(progression)
            break

        elif menu_selection == 4:
            staffVersion()
            verticalHistogram()
            print ()
            DisplayingList(progression)
            writingFile(progression)
            ReadFile()
            print ('\n                                       EXITING PROGRAM!!')
            break

        else:
            print ('Invalid Selection!! Try again using ONLY 1, 2, 3 and 4\n')  # If user enters an invalid input
    
    except ValueError:
        print ('Integer Required!  Try again using ONLY 1, 2, 3 and 4\n')















        


