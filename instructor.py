import os


class Instructor:
    def __init__(self, name, surname, age, workExp, Our_workExp):
        self.name = name
        self.surname = surname
        self.age = age
        self.workExp = workExp
        self.Our_workExp = Our_workExp
        
    def inputInstructor():
        name = input("Name: ")
        surname = input("Surname: ")
        while True:
                try:
                    age = int(input("Age: "))
                    if(age < 18):
                        print("Instructor can't be underaged")
                        continue
                    break
                except ValueError:
                    print("Age should be a number!")
        while True:
                try:
                    workExp = int(input("Work experience: "))
                    if(age - workExp < 18):
                        print("You can't work as instructor if you are underaged")
                        continue
                    break
                except ValueError:
                    print("Work expiriene should be a number!")
        while True:
                try:
                    Our_workExp = int(input("Our School Work Experience: "))
                    if(workExp - Our_workExp < 0):
                        print("Incorect data")
                        continue
                    break
                except ValueError:
                    print("Work expiriene should be a number!")
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
            instructor = Instructor(name, surname, age, workExp, Our_workExp)
            instructor.saveInstructor()
            print("Data saved to file!")
            input("Press Enter to continue...")
            os.system("CLS")
        else:
            print("Okey!")
    
    def saveInstructor(self):
        with open("Instructors.txt", "a", encoding="utf-8") as file:
            file.write(f"\nName: {self.name}\n")
            file.write(f"Surname: {self.surname}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Work Experience: {self.workExp}\n")
            file.write(f"Our School Work Experience: {self.Our_workExp}\n")
            file.write(f"------------------------------")

            
    def printInstructors():
        os.system("CLS")
        print('''
List of our Instructors:
------------------------------''')
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
                        del data[i:i+6]
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
        os.system("CLS")
        print("Work in progress!")
        input("Press Enter to continue...")
        os.system("CLS")
        
    def doMathInstructor(userChoice):
        if userChoice == 1:
            os.system("CLS")
            with open("Instructors.txt", 'r', encoding="utf8") as file:
                lines = file.readlines()

            print("Work experience before applying to our job")
            print("-----------------------------------------------")
            for i in range(0, len(lines), 6):
                name = lines[i].split(': ')[1].strip()
                surname = lines[i+1].split(': ')[1].strip()
                work_experience = int(lines[i+3].split(': ')[1].strip())
                school_experience = int(lines[i+4].split(': ')[1].strip())

                difference = work_experience - school_experience
                
                if difference == 0:
                    difference = "No experience"
                    print(f"{name} {surname}: {difference}")
                elif difference == 1:
                    print(f"{name} {surname}: {difference} year")
                else:
                    print(f"{name} {surname}: {difference} years")

        if userChoice == 2:
            os.system("CLS")
            print("Work in progress...")
        if userChoice == 3:
            os.system("CLS")
            print("Work in progress...")
        
        print()
        input("Press Enter to continue...")
        os.system("CLS")
            
    def sortingInstructor():
        print("Work in progress...")
