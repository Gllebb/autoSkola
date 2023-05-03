import os
from car import *
from instructor import *
from student import *


def MainMenu():
    while(True):
        print('''
Main menu:
------------------------------------------
Select one of the options:
------------------------------------------
1. Add data
2. View data
3. Delete data
4. Search data
5. Summary
6. Sort
7. Exit
------------------------------------------
            ''')
        while True:
            try:
                userChoise = int(input("Input: "))
                if(userChoise < 1 or userChoise > 7):
                    print("Number should be rounded between 1 and 7.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")   
        os.system("CLS")
        if(userChoise == 1):
            print('''
What type of data this will be?
------------------------------------------
1. About Instructors
2. About Cars
3. About Students
    ''')
            while True:
                try:
                    dataType = int(input("Input: "))
                    if(dataType < 1 or dataType > 3):
                        print("Number should be rounded between 1 and 3.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 3.")
            os.system("CLS")
            if(dataType == 1):
                Instructor.inputInstructor()
                
        elif(userChoise == 2):
            Instructor.printInstructors()
        
        elif(userChoise == 3):
            Instructor.deleteInstructor()
                
        elif(userChoise == 4):
            print("Work in progress!")
        elif(userChoise == 5):
            print("Work in progress!")
        elif(userChoise == 6):
            print("Work in progress!")
        elif(userChoise ==7):
            print("See you next time!")
            break



MainMenu()
