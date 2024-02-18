while True:
    car_ids = [1, 2, 3, 4, 5]
    car_names = {1: "Suzuki Cultus", 2: "Suzuki Alto", 3: "Toyota Corolla", 4: "Honda City", 5: "Honda Civic"}
    car_models = {1: 2020, 2: 2021, 3: 2020, 4: 2021, 5: 2020}
    car_rentals = {1: 2000, 2: 1500, 3: 3000, 4: 2500, 5: 3500}
    car_fuel = {1: 17, 2: 19, 3: 13, 4: 14, 5: 12}
    car_issued = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    dic = {}
    print("\t\t\t\t Welcome to the AIQ car rentals :: ")
    print("\t\t\t\t ======= Available cars ========")
    print("#  Car  Name           Model   Rent/hour   Fuel avg   Available ")
    for i in range(5):
        print(car_ids[i], "  ", car_names[car_ids[i]], "    ", car_models[car_ids[i]], "    ", car_rentals[car_ids[i]], "      ", car_fuel[car_ids[i]], "         ", car_issued[car_ids[i]])
    id = input('enter your id no : ')
    name = input('enter name ')
    dic[name]= id
    try:
        rent_input = input('Enter car to rent : ').title()
        for car_id, car_name in car_names.items():
            if car_name == rent_input:
                if car_issued[car_id] == 0:
                    print('Car is available')
                    car_issued[car_id] = 1
                else:
                    print('Car is not available')
                break
        else:
            print('Car not found')

        back_input = input('Enter car to return : ').title()
        for car_id, car_name in car_names.items():
            if car_name == back_input:
                if car_issued[car_id] == 1:
                    print('Car is returned, thank you')
                    car_issued[car_id] = 0
                break
        else:
            print('Car not found')
        print(dic)
        t = input('Wanna continue or quit (c/q) : ').lower()
        if t == 'q':
            break
    except ValueError:
        print('Please enter a valid input.')
