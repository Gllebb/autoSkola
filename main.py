import os
# from Car import *
from Instructor import *
# from student import *

os.system("clear")


def MainMenu():
  while (True):
    print('''
Driving school \"Splinter\"!
------------------------------------------
Main menu: (Add colors)
------------------------------------------
Select one of the options:
------------------------------------------
1. Add data
2. View data
3. Delete data
4. Search data ? (netu)
5. Do math ?
6. Sort ?
7. Exit
------------------------------------------''')
    while True:
      try:
        userChoise = int(input("Input: "))
        if (userChoise < 1 or userChoise > 7):
          print("Number should be rounded between 1 and 7.")
          continue
        break
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
    os.system("clear")

    # new part

    if (userChoise == 1):
      print('''
What type of data this will be?
------------------------------------------
1. About Instructors
2. About Cars
3. About Students
    ''')
      while True:
        try:
          userChoise1 = int(input("Input: "))
          if (userChoise1 < 1 or userChoise1 > 3):
            print("Number should be rounded between 1 and 3.")
            continue
          break
        except ValueError:
          print("Invalid input. Please enter a number between 1 and 3.")
      os.system("clear")
      if (userChoise1 == 1):
        Instructor.inputInstructor()
      elif userChoise1 == 2:
        print("Work in progress...")
      elif userChoise1 == 3:
        print("Work in progress...")
      else:
        print("Something went wrong:(")

# new part

    elif (userChoise == 2):
      print('''
What type of data this will be?
------------------------------------------
1. About Instructors
2. About Cars
3. About Students
    ''')
      while True:
        try:
          userChoise1 = int(input("Input: "))
          if (userChoise1 < 1 or userChoise1 > 3):
            print("Number should be rounded between 1 and 3.")
            continue
          break
        except ValueError:
          print("Invalid input. Please enter a number between 1 and 3.")

      if (userChoise1 == 1):
        Instructor.printInstructors()
      elif userChoise1 == 2:
        print("Work in progress...")
      elif userChoise1 == 3:
        print("Work in progress...")
      else:
        print("Something went wrong:(")

# new part

    elif (userChoise == 3):
      print('''
What type of data this will be?
------------------------------------------
1. About Instructors
2. About Cars ?
3. About Students ?
    ''')
      while True:
        try:
          userChoise1 = int(input("Input: "))
          if (userChoise1 < 1 or userChoise1 > 3):
            print("Number should be rounded between 1 and 3.")
            continue
          break
        except ValueError:
          print("Invalid input. Please enter a number between 1 and 3.")
      os.system("clear")
      if userChoise1 == 1:
        print('''
1. Delete specific data
2. Delete all the data
------------------------------------------
''')
        while True:
          try:
            userChoise2 = int(input("Input: "))
            if (userChoise2 < 1 or userChoise2 > 2):
              print("Number should be rounded between 1 and 2.")
              continue
            break
          except ValueError:
            print("Invalid input. Please enter a number between 1 and 2.")
        os.system("clear")
        if userChoise2 == 1:
          print('''
1. Serch by ID
2. Search by Name and Surname 
------------------------------------------
''')
          while True:
            try:
              userChoise3 = int(input("Input: "))
              if (userChoise3 < 1 or userChoise3 > 2):
                print("Number should be rounded between 1 and 2.")
                continue
              break
            except ValueError:
              print("Invalid input. Please enter a number between 1 and 2.")
          os.system("clear")
          if userChoise3 == 1:
            Instructor.deleteInstructor(1)
          if userChoise3 == 2:
            Instructor.deleteInstructor(3)
        elif userChoise2 == 2:
          Instructor.deleteInstructor(2)
          os.system("clear")
        else:
          print("Something went wrong:(")
      elif userChoise1 == 2:
        print("Work in progress...")
      elif userChoise1 == 3:
        print("Work in progress...")
      else:
        print("Something went wrong:(")

# new part

    elif (userChoise == 4):
      print('''
What type of data you want to search?
------------------------------------------
1. About Instructors
2. About Cars
3. About Students
''')
      userChoise = int(input("Enter there: "))
      print("Work in progress!")

# new part

    elif (userChoise == 5):
      print('''
1. Show Work expirience before applying to our job
2. Show at what age Instructor applied to his first job
3. Show amounth of years to his next anniversary''')
      userChoise = int(input("Enter there: "))
      Instructor.doMathInstructor(userChoise)

# new part

    elif (userChoise == 6):
      print('''
1. Sort People by the age from smallest to biggest
2. Sort People by the age from biggest to smallest
3. Sort People by the name from A to Z
4. Sort People by the name from Z to A
          ''')
      userChoise = int(input("Enter there: "))
      print("---------------------------------")
      Instructor.sortingInstructor(userChoise)


# new part

    elif (userChoise == 7):
      print("See you next time!")
      break

MainMenu()
