def add_record():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")

    # Create or open the file in append mode
    with open("records.txt", "a") as file:
        # Get the next unique ID by counting existing records
        unique_id = count_records() + 1
        # Write the record to the file
        file.write(f"{unique_id}, {name}, {phone_number}\n")
    print("Record added successfully!")


def count_records():
    try:
        # Open the file in read mode
        with open("records.txt", "r") as file:
            # Count the number of lines/records
            count = sum(1 for _ in file)
        return count
    except FileNotFoundError:
        # If file doesn't exist, return 0
        return 0


def main():
    while True:
        add_record()
        choice = input("Do you want to add another record? (yes/no): ")
        if choice.lower() != "yes":
            break


if __name__ == "__main__":
    main()
