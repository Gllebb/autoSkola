class Instructor:
    def __init__(self, name, surname, age, workExp):
        self.name = name
        self.surname = surname
        self.age = age
        self.workExp = workExp
        
    def printInstructor(self):
        print(f'''
Your inputed data:
------------------------------------------
1. Name = {self.name}
2. Surname = {self.surname}
3. Age = {self.age}
4. WorkExp = {self.workExp}
------------------------------------------
        ''')
        
    def saveInstructor(self):
        filename = "Instructors.txt"
        with open(filename, "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Surname: {self.surname}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Work Experience: {self.workExp}\n")
        print("Data saved to file.")



def AddData():
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
    print(dataType)
    if(dataType == 1):
        name = input("Name: ")
        surname = input("Surname: ")
        age = int(input("Age: "))
        workExp = int(input("Work experience: "))
        instructor1 = Instructor(name, surname, age, workExp)
        instructor1.printInstructor()
        instructor1.saveInstructor()




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
        
        if(userChoise == 1):
            print("Work in progress!")
            AddData()
        elif(userChoise == 2):
            print("Work in progress!")
        elif(userChoise == 3):
            print("Work in progress!")
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