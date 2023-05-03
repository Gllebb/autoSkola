import os
import json


class Instructor:
    def __init__(self, name, surname, age, workExp):
        self.name = name
        self.surname = surname
        self.age = age
        self.workExp = workExp
        
    def inputInstructor():
        name = input("Name: ")
        surname = input("Surname: ")
        age = int(input("Age: "))
        workExp = int(input("Work experience: "))
        print(f'''
------------------------------------------
If you want to save that data, input (1), if not, input (2).
        ''')
        while True:
                try:
                    userChoice = int(input("Input: "))
                    if(userChoice < 1 or userChoice > 2):
                        print("Number should be rounded between 1 and 2.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 2.")
        os.system("CLS")
        if(userChoice == 1):
            instructor = Instructor(name, surname, age, workExp)
            instructor.saveInstructor()
            print("Data saved to file!")
        else:
            print("Okey!")
    
    def saveInstructor(self):
        file = "Instructors.txt"
        with open(file, "a", encoding="utf-8") as file:
            file.write(f"\nName: {self.name}\n")
            file.write(f"Surname: {self.surname}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Work Experience: {self.workExp}\n")
            
    def printInstructors():
        os.system("CLS")
        with open("Instructors.txt", "r", encoding="utf-8") as file:
            data = file.read()
            print(data)
        input("Press Enter to continue...")
        os.system("CLS")
    
    def deleteInstructor(userChoise):
        filename = "Instructors.txt"
        if(userChoise == 1):
            print("111")
        elif(userChoise == 2):
            filename = "Instructors.txt"
            with open(filename, "r+", encoding="utf-8") as file:
                file.truncate(0)
            print("All the data was successfully deleted")
            input("Press Enter to continue...")
            os.system("CLS")
        else:
            print("error")
    
    def searchOrFilterInstructor():
        print("Work in progress!")
        
    def doMathInstructor():
        print("Work in progress!")
        
    def sortingInstructor():
        print("Work in progress!")
