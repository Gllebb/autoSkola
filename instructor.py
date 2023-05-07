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

    def deleteInstructor(userChoice):
        with open("Instructors.txt", "r+", encoding="utf-8") as filename:
            data = filename.readlines()
            if userChoice == 1:
                os.system("CLS")

                name = "Name: " + input("Enter the name: ")
                surname = "Surname: " + input("Enter the surname: ")

                for i in range(len(data)):
                    if name in data[i] and surname in data[i+1]:
                        found = True
                        del data[i:i+5]
                        filename.seek(0)
                        filename.truncate()
                        filename.writelines(data)
                        print(f"Data for {name} {surname} deleted")
                        break
                else:
                    print(f"No data found for {name} {surname}")
                    
                input("Press Enter to continue...")
                os.system("CLS")

            elif userChoice == 2:
                filename.truncate(0)
                print("All the data was successfully deleted")
                input("Press Enter to continue...")
                os.system("CLS")
            else:
                print("Error: Invalid choice")
                input("Press Enter to continue...")
                os.system("CLS")
    
    def searchOrFilterInstructor():
        print("Work in progress!")
        
    def doMathInstructor():
        print("Work in progress!")
        
    def sortingInstructor():
        print("Work in progress!")
