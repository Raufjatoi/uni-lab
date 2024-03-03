import datetime

class Car:
    def __init__(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

    def rent(self):
        self.available = False

    def return_car(self):
        self.available = True

def load_cars(filename):
    cars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                make, model, year, available = line.strip().split(',')
                car = Car(make, model, int(year), available == 'True')
                cars.append(car)
    except FileNotFoundError:
        print("File not found. Initializing with an empty list of cars.")
    return cars

def save_cars(filename, cars):
    with open(filename, "w") as file:
        for car in cars:
            file.write(f"{car.make},{car.model},{car.year},{car.available}\n")

def log_rental(filename, car, action):
    with open(filename, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp},{action},{car.make},{car.model},{car.year}\n")

def rent_car(cars):
    make = input("Enter the make of the car you want to rent: ")
    model = input("Enter the model of the car you want to rent: ")

    for car in cars:
        if car.make == make and car.model == model:
            if car.available:
                car.rent()
                save_cars("cars.txt", cars)
                log_rental("rental_log.txt", car, "Rented")
                print("Car rented successfully.")
            else:
                print("Sorry, this car is not available for rent.")
            return

    print("Car not found.")

def return_car(cars):
    make = input("Enter the make of the car you are returning: ")
    model = input("Enter the model of the car you are returning: ")

    for car in cars:
        if car.make == make and car.model == model:
            car.return_car()
            save_cars("cars.txt", cars)
            log_rental("rental_log.txt", car, "Returned")
            print("Car returned successfully.")
            return

    print("Car not found or already returned.")

def print_menu():
    print("\nCar Rental System Menu:")
    print("1. Rent a car")
    print("2. Return a car")
    print("3. Exit")

def main():
    cars = load_cars("cars.txt")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            rent_car(cars)
        elif choice == '2':
            return_car(cars)
        elif choice == '3':
            print("Thank you for using the car rental system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
