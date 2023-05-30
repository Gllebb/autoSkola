import os
from tabulate import tabulate


class Instructor:

  def __init__(self, name, surname, age, workExp, Our_workExp):
    self.name = name
    self.surname = surname
    self.age = age
    self.workExp = workExp
    self.Our_workExp = Our_workExp

  def inputInstructor():
    while True:
      name = input("Name (At least 2 letters): ")
      if len(name) < 2:
        print("Name can't be shorter than 2 letters")
      elif any(letter.isdigit() for letter in name):
        print("Name can't contain digits")
      else:
        break
    os.system("clear")

    while True:
      surname = input("Surname (At least 2 letters): ")
      if len(name) < 2:
        print("Surname can't be shorter than 2 letters")
      elif any(letter.isdigit() for letter in name):
        print("Surname can't contain digits")
      else:
        break
    os.system("clear")

    while True:
      try:
        age = int(input("Age (Instrucor has to be at least 18 years old): "))
        if (age < 18):
          print("Instructor can't be underaged")
          continue
        break
      except ValueError:
        print("Age should be a rounded number!")

    while True:
      try:
        workExp = int(input("Work experience: "))
        if (age - workExp < 18):
          print("You can't work as instructor if you are underaged")
          continue
        break
      except ValueError:
        print("Work expiriene should be a rounded number!")
    while True:
      try:
        Our_workExp = int(input("Our School Work Experience: "))
        if (workExp - Our_workExp < 0):
          print("Incorrect our school work expirience")
          continue
        break
      except ValueError:
        print("Work expiriene should be a rounded number!")
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
      instructor = Instructor(name, surname, age, workExp, Our_workExp)
      instructor.saveInstructor()
      print("Data saved to file!")
      input("Press Enter to continue...")
      os.system("clear")
    else:
      print("Okey!")

  def saveInstructor(self):
    with open("Instructors.txt", "r", encoding="utf-8") as file:
      data = file.readlines()

    last_instructor_id = 0
    for line in reversed(data):
      if line.startswith("ID:"):
        last_instructor_id = int(line.split(":")[1].strip())
        break

    new_instructor_id = last_instructor_id + 1
    with open("Instructors.txt", "a", encoding="utf-8") as file:
      file.write(f"\nID: {new_instructor_id}\n")
      file.write(f"Name: {self.name.capitalize()}\n")
      file.write(f"Surname: {self.surname.capitalize()}\n")
      file.write(f"Age: {self.age}\n")
      file.write(f"Work Experience: {self.workExp}\n")
      file.write(f"Our School Work Experience: {self.Our_workExp}\n")
      file.write(f"------------------------------")

  def printInstructors():
    print('List of our Instructors:')

    table_data = []
    with open("Instructors.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())
        work_experience = int(lines[i + 3].split(': ')[1].strip())
        school_experience = int(lines[i + 4].split(': ')[1].strip())
        table_data.append(
          [name, surname, age, work_experience, school_experience])

    headers = [
      'Name', 'Surname', 'Age', 'Work Experience', 'Our School Work Experience'
    ]
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

    input("Press Enter to continue...")
    os.system("clear")

  def deleteInstructor(userChoice3):
    os.system("clear")
    with open("Instructors.txt", "r+", encoding="utf-8") as filename:
      if userChoice3 == 1:
        data = filename.readlines()

        id_to_delete = input("Enter the ID of the instructor to delete: ")
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
          print(f"Instructor with ID {id_to_delete} deleted:")
          print(deleted_data)
        else:
          print(f"No data found for ID {id_to_delete}")

        input("Press Enter to continue...")
        os.system("clear")

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

        input("Press Enter to continue...")
        os.system("clear")

      elif userChoice3 == 2:
        password = "123456789"
        print("To do this you have to input a password")
        userPassword = input("Enter a password: ")
        if (password == userPassword):
          filename.truncate(0)
          print("All the data was successfully deleted")
          input("Press Enter to continue...")
          os.system("clear")
        else:
          print("Incorrect password")
          input("Press Enter to continue...")
          os.system("clear")
      elif userChoice3 == 1:
        print("work in progress")
      else:
        print("Error: Invalid choice")
        input("Press Enter to continue...")
        os.system("clear")

  def filterInstructor():
    with open("Instructors.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()

      filtered_data = []

      valid_filters = ['age', 'workExp', 'Our_workExp']
      while True:
        filter_data = input(
          "Enter the data to filter by (age, workExp, Our_workExp): ")
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
        data_value = int(lines[i + 3 +
                               ['age', 'workExp', 'Our_workExp'
                                ].index(filter_data)].split(': ')[1].strip())

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

  def doMathInstructor(userChoice):
    os.system("clear")
    if userChoice == 1:
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Work experience before applying to our job")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        work_experience = int(lines[i + 3].split(': ')[1].strip())
        school_experience = int(lines[i + 4].split(': ')[1].strip())

        difference = work_experience - school_experience

        if difference == 0:
          difference = "No experience"
          print(f"{name} {surname}: {difference}")
        elif difference == 1:
          print(f"{name} {surname}: {difference} year")
        else:
          print(f"{name} {surname}: {difference} years")

    if userChoice == 2:
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Show at what age Instructor applied to his first job")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())
        work_experience = int(lines[i + 3].split(': ')[1].strip())

        difference = age - work_experience

        print(f"{name} {surname}: {difference} years")

    if userChoice == 3:
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Show amount of years to his next anniversary")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        name = lines[i].split(': ')[1].strip()
        surname = lines[i + 1].split(': ')[1].strip()
        age = int(lines[i + 2].split(': ')[1].strip())

        nextAnniversary = (age // 10 + 1) * 10
        yearsToNextAnniversary = nextAnniversary - age

        if yearsToNextAnniversary == 10:
          print(
            f"{name} {surname}:Anniversary this year and in {yearsToNextAnniversary} years!"
          )
        elif yearsToNextAnniversary == 1:
          print(
            f"{name} {surname}: {yearsToNextAnniversary} year to next anniversary!"
          )
        else:
          print(
            f"{name} {surname}: {yearsToNextAnniversary} years to next anniversary!"
          )

    print()
    input("Press Enter to continue...")
    os.system("clear")

  def sortingInstructor(userChoice):
    # sorting by age from smallest to biggest
    if userChoice == 1:
      os.system("clear")
      print('People Are Sorted From smallest to biggest age')
      print("------------------------------")
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

        people = []
        current_person = {}
        for line in lines:
          line = line.strip()
          if line.startswith('Name:'):
            current_person['Name'] = line.split()[1]  # delete "Name: "
          elif line.startswith('Surname:'):
            current_person['Surname'] = line.split()[1]  # delete "Surname: "
          elif line.startswith('Age:'):
            current_person['Age'] = int(line.split()[1])  # delete "Age: "
          elif line.startswith('------------------------------'):
            people.append(current_person)
            current_person = {}

        sorted_people = sorted(people, key=lambda x: x['Age'])  # pēc kā sortēt

        for person in sorted_people:
          print(f"{person['Name']} {person['Surname']} {person['Age']}")

    # sorting by age from biggest to smallest
    elif userChoice == 2:
      os.system("clear")
      print('People Are Sorted From biggest to smallest age')
      print("------------------------------")
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

        people = []
        current_person = {}
        for line in lines:
          line = line.strip()
          if line.startswith('Name:'):
            current_person['Name'] = line.split()[1]
          elif line.startswith('Surname:'):
            current_person['Surname'] = line.split()[1]
          elif line.startswith('Age:'):
            current_person['Age'] = int(line.split()[1])
          elif line.startswith('------------------------------'):
            people.append(current_person)
            current_person = {}

        sorted_people = sorted(people, key=lambda x: x['Age'],
                               reverse=True)  # pēc kā sortēt

        for person in sorted_people:
          print(f"{person['Name']} {person['Surname']} {person['Age']}"
                )  # pēc kā sortēt

    # sorting by name from A to Z
    elif userChoice == 3:
      os.system("clear")
      print('People Are Sorted By Surname A-Z')
      print("------------------------------")
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

        people = []
        current_person = {}
        for line in lines:
          line = line.strip()
          if line.startswith('Name:'):
            current_person['Name'] = line.split()[1]
          elif line.startswith('Surname:'):
            current_person['Surname'] = line.split()[1]
          elif line.startswith('Age:'):
            current_person['Age'] = int(line.split()[1])
          elif line.startswith('------------------------------'):
            people.append(current_person)
            current_person = {}

        sorted_people = sorted(
          people,
          key=lambda x: x['Surname'],
        )  # pēc kā sortēt

        for person in sorted_people:
          print(f"{person['Name']} {person['Surname']} {person['Age']}")

    # sorting by name from Z to A
    elif userChoice == 4:
      os.system("clear")
      print('People Are Sorted By Surname Z-A')
      print("------------------------------")
      with open("Instructors.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

        people = []
        current_person = {}
        for line in lines:
          line = line.strip()
          if line.startswith('Name:'):
            current_person['Name'] = line.split()[1]
          elif line.startswith('Surname:'):
            current_person['Surname'] = line.split()[1]
          elif line.startswith('Age:'):
            current_person['Age'] = int(line.split()[1])
          elif line.startswith('------------------------------'):
            people.append(current_person)
            current_person = {}

        sorted_people = sorted(people,
                               key=lambda x: x['Surname'],
                               reverse=True)  # pēc kā sortēt

        for person in sorted_people:
          print(f"{person['Name']} {person['Surname']} {person['Age']}")

    print()
    input("Press Enter to continue...")
    os.system("clear")
