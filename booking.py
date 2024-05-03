import datetime

print("This is a simple app that helps you book a clinic visit.\n")
print("Please follow these simple prompts. Thank you\n")

def get_name():
    while True:
        name = input("What is your full name? \n").strip()
        if name:
            return name
        else:
            print("Name is required. Please try again.\n")

def get_age():
    while True:
        try:
            age = int(input("How old are you? (Age in years) \n"))
            return age
        except ValueError:
            print("Invalid age. Please enter a number.\n")

def get_gender():
    while True:
        gender = input("Are you Male or Female? Enter M for Male or F for Female \n").upper()
        if gender in ['M', 'F']:
            return 'Male' if gender == 'M' else 'Female'
        else:
            print("Invalid gender. Please enter M or F.\n")

def get_reason():
    while True:
        reason = input("What is your reason for booking?\n1. New session\n2. Review\n3. Prescription refill\nEnter 1, 2, or 3: \n")
        if reason in ['1', '2', '3']:
            reasons = ['New session', 'Review', 'Prescription refill']
            return reasons[int(reason) - 1]
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")

def get_date():
    while True:
        try:
            date_str = input("When do you want to see the doctor? \nPlease enter the date in the following format (DD-MM-YYYY) \n")
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
            if date >= datetime.date.today():
                return date
            else:
                print("Invalid date. Date must be today or in the future.\n")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.\n")

def get_time():
    while True:
        time_str = input("What time do you want to see the doctor? Select Time (HH:MM) \n")
        try:
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            return time
        except ValueError:
            print("Invalid time format. Please use HH:MM.\n")

name = get_name()
age = get_age()
gender = get_gender()
reason = get_reason()
booking_date = get_date()
booking_time = get_time()

print("\nThank you for booking with us. Here is a quick summary:\n")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Reason for booking: {reason}")
print(f"Appointment Date: {booking_date.strftime('%d-%m-%Y')}")
print(f"Appointment Time: {booking_time.strftime('%H:%M')}")

while True:
    confirm = input("\nPlease confirm your booking (Y/N): \n").upper()
    if confirm == 'Y':
        print("Your booking has been confirmed. Thank you!")
        break
    elif confirm == 'N':
        print("Booking cancelled. Thank you for using our app.")
        break
    else:
        print("Invalid input. Please enter Y or N.")



