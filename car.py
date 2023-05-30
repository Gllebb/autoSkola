import os
from tabulate import tabulate
import datetime


class Cars:

  def __init__(self, maker, model, releaseYear, carMileage,
               Our_schoolMileague):
    self.maker = maker
    self.model = model
    self.releaseYear = releaseYear
    self.carMileage = carMileage
    self.Our_schoolMileague = Our_schoolMileague

  def inputCar():
    while True:
      maker = input("Car manufacture name: (At least 2 letters): ")
      if len(maker) < 2:
        print("Car manufacture name can't be shorter than 2 letters")
      elif any(letter.isdigit() for letter in maker):
        print("Car manufacture name can't contain digits")
      else:
        break

    while True:
      model = input("Model: ")
      break

    while True:
      try:
        releaseYear = int(input("Release year (has to be at least 1894): "))
        if (releaseYear < 1894):
          print("Car can't be older than the oldest car(1894)")
          continue
        break
      except ValueError:
        print("Year should be a rounded number!")

    while True:
      try:
        carMileage = int(input("Car mileage: "))
        break
      except ValueError:
        print("Car mileage should be a rounded number!")

    while True:
      try:
        Our_schoolMileague = int(input("Our School car mileage: "))
        if (carMileage - Our_schoolMileague < 0):
          print("Incorrect our school car mileage")
          continue
        break
      except ValueError:
        print("Car mileage should be a rounded number!")
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
      cars = Cars(maker, model, releaseYear, carMileage, Our_schoolMileague)
      cars.saveCar()
      print("Data saved to file!")
      input("Press Enter to continue...")
      os.system("clear")
    else:
      print("Okey!")

  def saveCar(self):
    with open("Cars.txt", "r", encoding="utf-8") as file:
      data = file.readlines()

    lastCarID = 0
    for line in reversed(data):
      if line.startswith("ID:"):
        lastCarID = int(line.split(":")[1].strip())
        break

    newCarID = lastCarID + 1
    with open("Cars.txt", "a", encoding="utf-8") as file:
      file.write(f"\nID: {newCarID}\n")
      file.write(f"Maker: {self.maker.capitalize()}\n")
      file.write(f"Model: {self.model.capitalize()}\n")
      file.write(f"Release Year: {self.releaseYear}\n")
      file.write(f"Car mileage: {self.carMileage}\n")
      file.write(f"Our school car mileage: {self.Our_schoolMileague}\n")
      file.write(f"------------------------------------")

  def printCars():
    print('List of our cars:')

    table_data = []
    with open("Cars.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()
      for i in range(1, len(lines), 7):
        maker = lines[i].split(': ')[1].strip()
        model = lines[i + 1].split(': ')[1].strip()
        releaseYear = int(lines[i + 2].split(': ')[1].strip())
        carMileage = int(lines[i + 3].split(': ')[1].strip())
        Our_schoolMileague = int(lines[i + 4].split(': ')[1].strip())
        table_data.append(
          [maker, model, releaseYear, carMileage, Our_schoolMileague])

    headers = [
      'maker', 'model', 'releaseYear', 'carMileage', 'Our_schoolMileague'
    ]
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

    input("Press Enter to continue...")
    os.system("clear")

  def deleteCars(userChoice3):
    os.system("clear")
    with open("Cars.txt", "r+", encoding="utf-8") as filename:
      if userChoice3 == 1:
        data = filename.readlines()

        id_to_delete = input("Enter the ID of the car you want to delete: ")
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

      elif userChoice3 == 3:
        maker = "Maker: " + input("Enter the maker: ")
        model = "Model: " + input("Enter the model: ")

        for i in range(len(data)):
          if maker in data[i] and model in data[i + 1]:
            del data[i - 1:i + 6]
            filename.seek(0)
            filename.truncate()
            filename.writelines(data)
            print(f"Data for {maker} {model} deleted")
            break
        else:
          print(f"No data found for {maker} {model}")

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

  def filterCars():
    with open("Cars.txt", "r", encoding="utf-8") as file:
      lines = file.readlines()

      filtered_data = []

      valid_filters = ['releaseYear', 'carMileage', 'Our_schoolMileague']
      while True:
        filter_data = input(
          "Enter the data to filter by (releaseYear, carMileage, Our_schoolMileague): "
        )
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
                               ['releaseYear', 'carMileage', 'Our_workExp'
                                ].index(filter_data)].split(': ')[1].strip())

        if comparison_operator == "<" and data_value < value:
          filtered_data.append(lines[i:i + 6])
        elif comparison_operator == ">" and data_value > value:
          filtered_data.append(lines[i:i + 6])
        elif comparison_operator == "=" and data_value == value:
          filtered_data.append(lines[i:i + 6])

      if filtered_data:
        print("\nFiltered Cars Data:")
        print("------------------------------")
        for car in filtered_data:
          print(''.join(car))
          print("------------------------------")
      else:
        print("No data found matching the provided criteria.")

    input("Press Enter to continue...")
    os.system("clear")

  def doMathCars(userChoice):
    os.system("clear")
    today = datetime.date.today()
    year = today.year
    if userChoice == 1:
      with open("Cars.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Car mileage before our driving school")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        maker = lines[i].split(': ')[1].strip()
        model = lines[i + 1].split(': ')[1].strip()
        carMileage = int(lines[i + 3].split(': ')[1].strip())
        Our_schoolMileague = int(lines[i + 4].split(': ')[1].strip())

        difference = carMileage - Our_schoolMileague

        if difference == 0:
          difference = "No mileague in our school"
          print(f"{maker} {model}: {difference}")
        elif difference == 1:
          print(f"{maker} {model}: {difference} mile")
        else:
          print(f"{maker} {model}: {difference} miles")

    if userChoice == 2:
      with open("Cars.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Average cars mileague per year")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        maker = lines[i].split(': ')[1].strip()
        model = lines[i + 1].split(': ')[1].strip()
        releaseYear = int(lines[i + 2].split(': ')[1].strip())
        carMileage = int(lines[i + 3].split(': ')[1].strip())

        average = carMileage / (year - releaseYear)
        print(f"{maker} {model}: {round(average, 2)} miles")

    if userChoice == 3:
      with open("Cars.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

      print("Show how old is car")
      print("-----------------------------------------------")
      for i in range(1, len(lines), 7):
        maker = lines[i].split(': ')[1].strip()
        model = lines[i + 1].split(': ')[1].strip()
        releaseYear = int(lines[i + 2].split(': ')[1].strip())

        difference = year - releaseYear

        if difference == 0:
          print(f"{maker} {model}: is a completely new car")
        elif difference == 1:
          print(f"{maker} {model}: is a {difference} year old car!")
        else:
          print(f"{maker} {model}: is a {difference} years old car!")

    print()
    input("Press Enter to continue...")
    os.system("clear")

  def sortCars(userChoice):

    if userChoice in [1, 2, 3, 4]:
      os.system("clear")
      if userChoice == 1:
        print('Cars Sorted From oldest to newest release year')
      elif userChoice == 2:
        print('Cars Sorted From newest to oldest release year')
      elif userChoice == 3:
        print('Cars are Sorted By Model Name (A-Z)')
      elif userChoice == 4:
        print('Cars are Sorted By Model Name (Z-A)')
        
      print("------------------------------")
      with open("Cars.txt", 'r', encoding="utf8") as file:
        lines = file.readlines()

        cars = []
        current_car = {}
        for line in lines:
          line = line.strip()
          if line.startswith('Maker:'):
            current_car['Maker'] = line.split(":")[1].strip()
          elif line.startswith('Model:'):
            current_car['Model'] = line.split(":")[1].strip()
          elif line.startswith('Release Year:'):
            current_car['releaseYear'] = int(line.split(":")[1].strip())
          elif line.startswith('------------------------------'):
            cars.append(current_car)
            current_car = {}

        if userChoice == 1:
          sorted_cars = sorted(cars, key=lambda x: x['releaseYear'])
        elif userChoice == 2:
          sorted_cars = sorted(cars, key=lambda x: x['releaseYear'], reverse=True)
        elif userChoice == 3:
          sorted_cars = sorted(cars, key=lambda x: x['Model'])
        elif userChoice == 4:
          sorted_cars = sorted(cars, key=lambda x: x['Model'], reverse=True)
          
        for car in sorted_cars:
          print(f"{car['Maker']} {car['Model']}: {car['releaseYear']}")

    print()
    input("Press Enter to continue...")
    os.system("clear")
