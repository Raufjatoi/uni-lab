import datetime

def log_visitor():
    # Open the file in append mode
    with open("visitor_log.txt", "a") as file:
        # Ask user for visitor details
        name = input("Enter visitor's name: ")
        phone_number = input("Enter visitor's phone number: ")
        
        # Get current timestamp
        arrival_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write visitor log to file
        file.write(f"Name: {name}, Phone: {phone_number}, Arrival Time: {arrival_time}\n")
        print("Visitor logged successfully.")

# Main function to execute the program
def main():
    log_visitor()

if __name__ == "__main__":
    main()
