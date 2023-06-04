import os
from tabulate import tabulate


class Student:

  def __init__(self, name, surname, age, DrivNeed, DrivDone):
    self.name = name
    self.surname = surname
    self.age = age
    self.DrivNeed = DrivNeed
    self.DrivDone = DrivDone

  def inputStudent():
    while True:
      name = input("Name (At least 2 letters): ")
      if len(name) < 2:
        print("Name can't be shorter than 2 letters")
      elif any(letter.isdigit() for letter in name):
        print("Name can't contain digits")
      else:
        break

    while True:
      surname = input("Surname (At least 2 letters): ")
      if len(surname) < 2:
        print("Surname can't be shorter than 2 letters")
      elif any(letter.isdigit() for letter in surname):
        print("Surname can't contain digits")
      else:
        break

    while True:
      try:
        age = int(input("Age (Student has to be at least 16 years old): "))
        if (age < 16 or age > 116):
          print("Student age is incorrect")
          continue
        break
      except ValueError:
        print("Age should be a rounded number!")

    while True:
      try:
        DrivNeed = int(input("Driving Needed: "))
        if DrivNeed != 10:
          print("You Should have 10 drivings ")
          continue
        break
      except ValueError:
        print("Number of drivings should be rounded!")
    while True:
      try:
        DrivDone = int(input("Driving Done: "))
        if DrivDone < 0 and DrivDone > 10:
          print("Incorrect driving done number")
          continue
        break
      except ValueError:
        print("Number of drivings should be rounded!")
    print(f'''
------------------------------------------
If you want to save that data, input (1), if not, input (2).
''')
    while True:
      try:
        userChoice = int(input("Input: "))
        if (userChoice < 1 or userChoice > 2):
          print("Number should be rounded between 1 and 2.")
          continue
        break
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 2.")
    os.system("clear")
    if (userChoice == 1):
      student = Student(name, surname, age, DrivNeed, DrivDone)
      student.saveStudent()
      print("Data saved to file!")
      input("Press Enter to continue...")
      os.system("clear")
    else:
      print("Okey!")

  def saveStudent(self):
    with open("Students.txt", "r", encoding="utf-8") as file:
      data = file.readlines()

    last_student_id = 0
    for line in reversed(data):
      if line.startswith("ID:"):
        last_student_id = int(line.split(":")[1].strip())
        break

    new_student_id = last_student_id + 1
    with open("Students.txt", "a", encoding="utf-8") as file:
      file.write(f"\nID: {new_student_id}\n")
      file.write(f"Name: {self.name.capitalize()}\n")
      file.write(f"Surname: {self.surname.capitalize()}\n")
      file.write(f"Age: {self.age}\n")
      file.write(f"Driving Needed: {self.DrivNeed}\n")
      file.write(f"Driving Done: {self.DrivDone}\n")
      file.write(f"------------------------------")

  def printStudent():
    print('List of our Students:')

    table_data = []
    with open("Students.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())
        driving_needed = int(lines[i + 3].split(': ')[1].strip())
        driving_done = int(lines[i + 4].split(': ')[1].strip())
        table_data.append([name, surname, age, driving_needed, driving_done])

    headers = ['Name', 'Surname', 'Age', 'Driving Needed', 'Driving Done']
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

    input("Press Enter to continue...")
    os.system("clear")

  def deleteStudent(userChoice3):
    os.system("clear")
    with open("Students.txt", "r+", encoding="utf-8") as filename:
      data = filename.readlines()
      if userChoice3 == 1:

        id_to_delete = input("Enter the ID of the student to delete: ")
        found = False
        deleted_data = ""

        for i in range(len(data)):
          if data[i].startswith("ID: ") and data[i].strip().split(
              ": ")[1] == id_to_delete:
            deleted_data = "".join(data[i - 1:i + 6])
            del data[i - 1:i + 6]
            found = True
            break

        if found:
          filename.seek(0)
          filename.truncate()
          filename.writelines(data)
          os.system("clear")
          print(f"Student with ID {id_to_delete} deleted:")
          print(deleted_data)
        else:
          print(f"No data found for ID {id_to_delete}")

      elif userChoice3 == 3:
        name = "Name: " + input("Enter the name: ")
        surname = "Surname: " + input("Enter the surname: ")

        for i in range(len(data)):
          if name in data[i] and surname in data[i + 1]:
            del data[i - 1:i + 6]
            filename.seek(0)
            filename.truncate()
            filename.writelines(data)
            print(f"Data for {name} {surname} deleted")
            break
        else:
          print(f"No data found for {name} {surname}")

      elif userChoice3 == 2:
        password = "123456789"
        print("To do this you have to input a password")
        userPassword = input("Enter a password: ")
        if (password == userPassword):
          filename.truncate(0)
          print("All the data was successfully deleted")
        else:
          print("Incorrect password")
      else:
        print("Error: Invalid choice")

      input("Press Enter to continue...")
      os.system("clear")

  def filterStudent():
    with open("Students.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()

      filtered_data = []

      valid_filters = ['age', 'DrivDone']
      while True:
        filter_data = input("Enter the data to filter by (age, DrivDone): ")
        if filter_data in valid_filters:
          break
        else:
          print("Invalid input. Please try again.")
      os.system("clear")

      valid_comparison = ['<', '>', '=']
      while True:
        comparison_operator = input(
          "Enter the comparison operator (<, >, =): ")
        if comparison_operator in valid_comparison:
          break
        else:
          print("Invalid input. Please try again.")
      os.system("clear")

      while True:
        try:
          value = int(input("Enter the value: "))
          break
        except ValueError:
          print("Invalid input. Please enter a number")
      os.system("clear")

      for i in range(0, len(lines), 7):
        data_value = int(
          lines[i + 3 +
                ['age', 'DrivDone'].index(filter_data)].split(': ')[1].strip())

        if comparison_operator == "<" and data_value < value:
          filtered_data.append(lines[i:i + 6])
        elif comparison_operator == ">" and data_value > value:
          filtered_data.append(lines[i:i + 6])
        elif comparison_operator == "=" and data_value == value:
          filtered_data.append(lines[i:i + 6])

      if filtered_data:
        print("\nFiltered Instructor Data:")
        print("------------------------------")
        for instructor in filtered_data:
          print(''.join(instructor))
          print("------------------------------")
      else:
        print("No data found matching the provided criteria.")

    input("Press Enter to continue...")
    os.system("clear")

  def doMathStudent(userChoice):
    os.system("clear")
    if userChoice == 1:
      with open("Students.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Amount of remaining drives")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        driving_needed = int(lines[i + 3].split(': ')[1].strip())
        driving_done = int(lines[i + 4].split(': ')[1].strip())

        difference = driving_needed - driving_done

        if difference == 0:
          difference = "No drives"
          print(f"{name} {surname}: {difference}")
        elif difference == 1:
          print(f"{name} {surname}: {difference} drives")
        else:
          print(f"{name} {surname}: {difference} drives")

    if userChoice == 2:
      with open("Students.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Show amount of hours left")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())
        DrivDone = int(lines[i + 4].split(': ')[1].strip())

        difference = DrivDone * 1.5

        print(f"{name} {surname}: {difference} hours left")

    if userChoice == 3:
      with open("Students.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Show if he is to driving exam")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())
        driving_needed = int(lines[i + 3].split(': ')[1].strip())
        driving_done = int(lines[i + 4].split(': ')[1].strip())

        difference = driving_needed - driving_done

        if difference == 0:
          print(f'{name} {surname} - Ready for exam')
        elif difference != 0:
          print(f'{name} {surname} - Not ready for exam')

    print()
    input("Press Enter to continue...")
    os.system("clear")

  def sortingStudent(userChoice):
    # Sorting options based on userChoice
    if userChoice in [1, 2, 3, 4]:
        os.system("clear")
        if userChoice == 1:
            print('People Are Sorted From smallest to biggest age')
        elif userChoice == 2:
            print('People Are Sorted From biggest to smallest age')
        elif userChoice == 3:
            print('People Are Sorted By Surname A-Z')
        elif userChoice == 4:
            print('People Are Sorted By Surname Z-A')
        print("------------------------------")
        
        # Helper function to retrieve the 'Age' attribute from a person dictionary
        def get_age(person):
            return person['Age']
        
        def get_surname(person):
            return person['Surname']
        
        with open("Students.txt", 'r', encoding="utf8") as file:
            lines = file.readlines()

            people = []  # List to store information about each person
            current_person = {}  # Dictionary to hold details of an individual person
            for line in lines:
                line = line.strip()
                if line.startswith('Name:'):
                    # Extract the person's name and assign it to the 'Name' key in current_person dictionary
                    current_person['Name'] = line.split()[1]
                elif line.startswith('Surname:'):
                    # Extract the person's surname and assign it to the 'Surname' key in current_person dictionary
                    current_person['Surname'] = line.split()[1]
                elif line.startswith('Age:'):
                    # Extract the person's age, convert it to an integer, and assign it to the 'Age' key
                    current_person['Age'] = int(line.split()[1])
                elif line.startswith('------------------------------'):
                    # When encountering the separator line, add the current_person to the people list
                    people.append(current_person)
                    current_person = {}  # Reset current_person for the next person's information

            if userChoice == 1:
                # Sort people based on age in ascending order
                sorted_people = sorted(people, key=get_age)
            elif userChoice == 2:
                sorted_people = sorted(people, key=get_age, reverse=True)
            elif userChoice == 3:
                # Sort people based on surname in ascending order
                sorted_people = sorted(people, key=get_surname)
            elif userChoice == 4:
                sorted_people = sorted(people, key=get_surname, reverse=True)

            for person in sorted_people:
                print(f"{person['Name']} {person['Surname']} {person['Age']}")


    print()
    input("Press Enter to continue...")
    os.system("clear")
