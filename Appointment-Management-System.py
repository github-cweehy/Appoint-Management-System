import os
from datetime import datetime, timedelta

appointment_count = 0
full_appointment_count = 0
max_appointment = 100
count = 0
username = ""
code = ""

class Schedule:
    def __init__(self, date, time, service, name, phone, doctor):
        self.date = date
        self.time = time
        self.service = service
        self.name = name
        self.phone = phone
        self.doctor = doctor

def selectDate():
    pass
def selectTime():
    pass
def selectService():
    pass
def selectDoctor(date, time):
    pass
def addAppointment():
    pass
def getname():
    pass
def getphone():
    pass

date = selectDate()
time = selectTime()
service = selectService()
doctor = selectDoctor(date, time)
name = getname()
phone = getphone()

schedule_list = [Schedule(date,time,service,doctor,name,phone) for _ in range(max_appointment)]
full_appointment = [Schedule(date,time,service,doctor,name,phone) for _ in range(max_appointment)]


# Function for the main menu
def home() :
    print ("============================================================")
    print ("\t\tWELCOME TO TRIANGLE")
    print ("============================================================")
	
    print("\n\n1. REGISTER\n2. LOGIN\n3. ADMIN LOGIN\n4. Exit")

    choice = input("\n\nEnter your choice: ")

    if choice == '1' :
        reg()
    
    elif choice == '2':
        login()

    elif choice == '3':
        adminLogin()

    elif choice == '4':
        exit(0)
    else :
        choice = input("\n\nInvalid choice, please re-enter your choice : ")
        home()

# Function for user registration
import os

def reg():
    os.system('cls')  # Assuming you are using Windows. For Linux, you can use 'clear'.

    global username

    print("============================================================")
    print("\n\t\tRegister Account")
    print("\n============================================================")

    while True:
        username = input("\n\nEnter username (Maximum 20 characters): ")

        if username_validation():
            print("\nUsername is already taken. Please choose another username.")
            continue

        password = input("Enter password (Must be between 1 and 20 characters): ")

        len_username = len(username)
        len_password = len(password)

        if (1 <= len_username <= 20) and (1 <= len_password <= 20):
            break
        else:
            print("\nInvalid input. Username and password must be between 1 and 20 characters.")

    # Open a file for writing user details
    with open('user_details.txt', 'a+') as file1:
        # Write each username and password followed by a separator
        file1.write(f"Username: {username}\nPassword: {password}\n{'-' * 30}\n")
        print("\nRegister successfully!")

    # Prompt the user to log in or return to the home menu
    while True:
        login_status = input("\nLogin now? [Y/N]: ")
        if login_status.lower() == 'y':
            login()
            break
        elif login_status.lower() == 'n':
            home()
            break
        else:
            print("\nInvalid selection. Please enter 'Y' for Yes or 'N' for No.")


# Function for user login
def login():
    global username

    os.system('cls')  # Assuming you are using Windows. For Linux, you can use 'clear'.
    print("============================================================")
    print("\n\t\t\tLogin")
    print("\n============================================================")

    # Variable to track if the user is found
    found_user = False

    # Prompt username and password
    while True:
        entered_username = input("\nEnter username: ")
        entered_password = input("Enter password: ")

        # Verify username and password against stored user details in a file
        with open('user_details.txt', 'r') as file1:
            check_user = False  # Flag to indicate if we are checking the correct user

            for line in file1:
                if "Username:" in line:
                    username = line.split('Username: ')[1].strip()
                    check_user = (entered_username.strip() == username.strip())
                elif "Password:" in line and check_user:
                    password = line.split('Password: ')[1].strip()

                    if entered_password.strip() == password.strip():
                        found_user = True
                        break

            file1.close()

        if found_user:
            print("\nLogin successful\n")
            load_file()  # Load user appointment details
            loadAdminAppointmentsToFile()
            display_user_home()
            break
        else:
            print("\nThe username or password you entered is incorrect. Please try again.\n")



# Function for admin login
def adminLogin():
    global code
    i = 0

    while (i<1):
        code = input("\nYour admin ID : ")

        # Check if the entered code matches one of the valid admin IDs
        if code in [ "1221204416" , "1221204572" , "1221205257"]:
            
            # Set i to 1 to exit the loop
            i += 1

            # Load admin appointments data
            loadAdminAppointmentsToFile()

            # Display the user's home menu
            display_admin_home()

        elif (code == "B" or code == "b"):
            
            # Set i to 1 to exit the loop
            i += 1

            # Go back to the home menu
            home()
        
        else:

            # Display an error message for an incorrect admin ID and allow the user to try again
            print("\nWrong ID. Please try again. (Enter B back to home)\n")

# Function to display the user's home screen
def display_user_home():

    global appointment_count, full_appointment_count, code
    choice_doc = ""

    # Flag to control menu display
    displayMenu = True
    while True:
        if(displayMenu):
            print("\n=========================================================")
            print("\n\t\tMenu Selection")
            print("\n=========================================================")
            print("\n1. Add Appointment")
            print("\n2. Edit Apointment")
            print("\n3. Delete/Cancel Appointment")
            print("\n4. View Appointment")
            print("\n5. Search Appointment")
            print("\n6. Logout")
            print("\n7. Exit") 
        
        choice2 = input("\n\nEnter your choice : ")

        if (choice2 == '1'):
            # Call a function to add a new appointment
            addAppointment()

        elif (choice2 == '2'):
            # Call a function to edit an existing appointment
            editAppointment()

        elif (choice2 == '3'):
            # Call a functin to delete/cancel an appointment
            deleteAppointment()
        
        elif (choice2 == '4'):
            # Call a function to view appointments (user)
            viewAppointment()
        
        elif (choice2 == '5'):
            # Call a function to search appointments(user)
            searchAppointments()
        
        elif (choice2 == '6'):

            # Reset schedule count
            appointment_count = 0

            #Reset admin schedule count
            full_appointment_count = 0

            # Clear the admin code
            code = ""

            # Go back to the home menu
            home()

        elif (choice2 == '7'):
            # Exit the program
            exit(0)
        
        else:
            print("\nInvalid selection! Please enter a valid choice.\n")
            # Do not display the menu on invalid selection
            displayMenu = False

        if (choice2 >= '1' and choice2 <= '7'):
            # Display the menu on valid selections
            displayMenu = True
        
def display_admin_home():
    displayMenu = True
    global appointment_count, full_appointment_count, code
    
    while True:
        if displayMenu:
            print("\n=========================================================")
            print("\n\t\tMenu Selection")
            print("\n=========================================================")
            print("\n1. Add User Appointment")
            print("\n2. Edit User Appointment")
            print("\n3. Delete User Appointment")
            print("\n4. View User Appointment")
            print("\n5. View All Appointments")
            print("\n6. Search Appointments")
            print("\n7. Logout")
            print("\n8. Exit")

        choice2 = input("\n\nEnter your choice: ")

        if choice2 == '1':
            # Call a function to add user appointments (admin)
            addUserAppointment()

        elif choice2 == '2':
            # Call a function to edit user appointments (admin)
            editUserAppointment()

        elif choice2 == '3':
            # Call a function to delete user appointments (admin)
            deleteUserAppointment()

        elif choice2 == '4':
            # Call a function to view user appointments (admin)
            viewUserAppointment()

        elif choice2 == '5':
            # Call a function to view all appointments (admin)
            viewAllAppointment()

        elif choice2 == '6':
            # Call a function to search all appointments by name (admin)
            searchAllAppointments()

        elif choice2 == '7':
            # Reset schedule count
            appointment_count = 0

            # Reset admin schedule count
            full_appointment_count = 0

            # Clear the admin code
            code = ""

            # Go back to the home menu
            home()

        elif choice2 == '8':
            exit(0)

        else:
            print("\nInvalid selection! Please enter a valid choice.\n")
            # Do not display the menu on invalid selection
            displayMenu = False

        if '1' <= choice2 <= '7':
            # Display the menu on valid selections
            displayMenu = True


def addAppointment():

    global appointment_count, full_appointment_count
    

    # Function to select the desried medical service for the appointment
    service = selectService()

    # Function to select the appointment date
    date = selectDate()

    # Function to select the appointment time
    time = selectTime()

    # Function to select the doctor for the appointment
    doctor = selectDoctor(date, time)

    # Validate if the selected appointment time is available and doctor is selected
    if (time_validation(date, time, doctor) and len(doctor) > 1):
        
        name = getname()
        phone = getphone()

        print("\nDate               : {}".format(date))
        print("\nTime               : {}".format(time))
        print("\nService            : {}".format(service))
        print("\nDoctor             : {}".format(doctor))
        print("\nYour name          : {}".format(name))
        print("\nYour phone number  : {}".format(phone))
        
        confirm = input("\n\nAppointment confirmation [Y|N] : ")
        if (confirm == 'y' or confirm == 'Y'):

            # Copy the appointment details into a new appointment class
            new_appointment = Schedule(date, time, service, name, phone, doctor)

            # Check if the maximum appointment limit has been reached
            if (appointment_count < max_appointment):

                # Add the new appointment to the schedule list
                schedule_list [appointment_count] = new_appointment
                appointment_count += 1

                # Add the new appointment to the full appointment list
                full_appointment [full_appointment_count] = new_appointment
                full_appointment_count += 1

                # Save the updated appointments to a file
                saveAppointmentsToFile()
                saveAdminAppointmentsToFile()
                print ("\nAppointment scheduled successfully.\n")

            else:
                print("Maximum appointment limit reached. Cannot schedule.\n")

        else:
            print("\nNo appointment was schedule.")
            if code in [ "1221204416" , "1221204572" , "1221205257"]:
                display_admin_home()
            display_user_home()   

    else:
        print ("\nThe selected time slot is fully booked or the doctor is not available. Please choose another time or doctor.\n")

def editAppointment():
    global appointment_count, full_appointment_count
    global max_appointment, count

    doctors = {"Doctor Wee", "Doctor Lye", "Doctor Tan"}

    print("\n======================================")
    print("\n\tEdit Appointment")
    print("\n======================================")

    if appointment_count > 0:

        # Display the user's appointments
        print("\nYour Appointments:\n")
        viewAppointment()

        choice = int(input("\nEnter the number of the appointment you want to edit (1 to {}): ".format(appointment_count)))

        if 1 <= choice <= appointment_count:
            # Adjust the choice to patch the array index
            choice -= 1

            # Prompt the user to select new service, date, time, and doctor
            service = selectService()
            date = selectDate()
            time = selectTime()
            doctor = selectDoctor(date, time)

            if choice_doc == 'N' or choice_doc == 'n':
                doctor_assigned = False
                for doc in doctors:
                    doctorAlreadyBooked = any(
                        appt.date == date
                        and appt.time == time
                        and appt.doctor == doc
                        for appt in full_appointment
                    )

                    if not doctorAlreadyBooked:
                        doctor = doc
                        doctor_assigned = True
                        break

                if not doctor_assigned:
                    print("All doctors are booked at the selected date and time. Failed to assign a doctor.")
                    return

            # Check if the new time slot is valid and available
            if timevalidation2(date, time, doctor, choice):
                name = input("\nEnter your name: ")
                phone = input("\nEnter your phone number: ")

                print("\nDate               : {}".format(date))
                print("\nTime               : {}".format(time))
                print("\nService            : {}".format(service))
                print("\nDoctor             : {}".format(doctor))
                print("\nYour name          : {}".format(name))
                print("\nYour phone number  : {}".format(phone))

                confirm = input("\n\nAppointment confirmation [Y|N] : ")

                if confirm.lower() == 'y':
                    print("")
                else:
                    print("\nNo appointment was edited.")
                    if code in [ "1221204416" , "1221204572" , "1221205257"]:
                        display_admin_home()
                    display_user_home()

                # Update the appointment details
                new_appointment = Schedule(date, time, service, name, phone, doctor)

                # Replace the old appointment with the new one
                schedule_list[choice] = new_appointment
                full_appointment[choice] = new_appointment

                # Save appointments to file after editing
                saveAppointmentsToFile()
                saveAdminAppointmentsToFile2()
                print("\nAppointment scheduled successfully.\n")

            # The slot is already booked
            else:
                print("The selected time slot is already booked. Failed to edit appointment.\n")

        else:
            print("\nInvalid selection. Failed to edit appointment.\n")

    else:
        print("\nNo appointments to edit.\n")


def deleteAppointment():
    global appointment_count, full_appointment_count

    print("\n======================================")
    print("\n\tDelete Appointment")
    print("\n======================================")

    # Display the user's appointments
    if appointment_count > 0:
        print("\nYour appointments:\n")
        viewAppointment()

        # Ask the user for the appointment number they want to delete
        choice = int(input("\nEnter the number of the appointment you want to delete (1 to {}): ".format(appointment_count)))

        # Validate the user's choice
        if 1 <= choice <= appointment_count:
            # Adjust the choice to match the array index
            choice -= 1

            # Remove the appointment from the schedule list
            removed_appointment = schedule_list.pop(choice)

            # Find the index of the appointment in full_appointment
            index_to_remove = -1
            for count in range(full_appointment_count):
                if full_appointment[count].date == removed_appointment.date and \
                        full_appointment[count].time == removed_appointment.time and \
                        full_appointment[count].doctor == removed_appointment.doctor:
                    index_to_remove = count
                    break

            if index_to_remove != -1:
                # Remove the appointment from the full appointment list
                full_appointment.pop(index_to_remove)
                # Update the full_appointment_count variable
                full_appointment_count -= 1
                # Update the appointment_count variable
                appointment_count -= 1

                # Save appointments to file after deleting
                saveAppointmentsToFile()
                saveAdminAppointmentsToFile()

                # Display a confirmation message
                print("\nAppointment has been deleted/cancelled.\n")
            else:
                print("Appointment not found in the full appointment list.")

        else:
            # Display an error message for an invalid choice
            print("\nInvalid choice.\n")

    else:
        # Display a message when there are no appointments to delete
        print("\nNo appointments to delete.\n")


def viewAppointment():
    print("\n====================================================================================================================================")
    print("\n\t\t\t\t\t\tAppointment Schedule")
    print("\n====================================================================================================================================")

    # Initialize the schedule_list
    schedule_list = []

    try:
        # Open the file for reading
        with open(f"{username}.txt", "r") as file:
            appointment_data = {}
            for line in file:
                # Check if the line contains a label
                if ":" in line:
                    label, value = map(str.strip, line.split(":", 1))
                    appointment_data[label] = value
                elif line.strip() == '-' * 30:
                    # Create a Schedule object and add it to the schedule_list
                    if all(key in appointment_data for key in ['Service', 'Date', 'Time', 'Doctor', 'Name', 'Phone']):
                        appointment = Schedule(
                            appointment_data['Date'],
                            appointment_data['Time'],
                            appointment_data['Service'],
                            appointment_data['Name'],
                            appointment_data['Phone'],
                            appointment_data['Doctor']
                        )
                        schedule_list.append(appointment)
                    # Reset appointment_data for the next appointment
                    appointment_data = {}
                else:
                    # Skip lines without labels or separators
                    continue

        file.close()

    except FileNotFoundError:
        # If the file cannot be opened (doesn't exist), display a message
        print("| {:<102} |".format("No record found."))
        print("====================================================================================================================================\n")
        return

    # Display appointments if any
    if schedule_list:
        print("\n| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format("No.", "Date", "Time", "Service", "Doctor", "Name", "Phone Number"))
        print("\n------------------------------------------------------------------------------------------------------------------------------------")

        # Loop through and display each appointment
        for count, appointment in enumerate(schedule_list, start=1):
            print("| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format(
                count, appointment.date, appointment.time, appointment.service,
                appointment.doctor, appointment.name, appointment.phone))

        print("====================================================================================================================================\n")

    else:
        # Display a message when there are no appointments
        print("| {:<102} |".format("No record found."))
        print("====================================================================================================================================\n")


def viewAllAppointment():
    print("\n====================================================================================================================================")
    print("\n\t\t\t\t\t\tAppointment Schedule")
    print("\n====================================================================================================================================")

    # Filter out appointments with missing or invalid values
    valid_appointments = [appointment for appointment in full_appointment if all([appointment.date, appointment.time])]

    if valid_appointments:
        # Sort the valid_appointments list by date and time
        valid_appointments.sort(key=lambda x: ((x.date or ''), (x.time or '')))

        # Print the header
        print("\n| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format("No.", "Date", "Time", "Service", "Doctor", "Name", "Phone Number"))
        print("\n------------------------------------------------------------------------------------------------------------------------------------")

        # Loop through and display each valid appointment
        for count, appointment in enumerate(valid_appointments, start=1):
            print("| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format(
                count, appointment.date, appointment.time, appointment.service,
                appointment.doctor, appointment.name, appointment.phone))

        print("====================================================================================================================================\n")
    
    else:
        # Display a message when there are no valid appointments
        print("| {:<102} |".format("No valid record found."))
        print("====================================================================================================================================\n")



def saveAppointmentsToFile():
    # Create a file name based on the user's username
    file_name = f"{username}.txt"

    # Open the file for writing
    try:
        with open(file_name, "w") as file:
            for count in range(appointment_count):
                file.write(f"Service: {schedule_list[count].service}\n"
                           f"Date:    {schedule_list[count].date}\n"
                           f"Time:    {schedule_list[count].time}\n"
                           f"Doctor:  {schedule_list[count].doctor}\n"
                           f"Name:    {schedule_list[count].name}\n"
                           f"Phone:   {schedule_list[count].phone}\n"
                           f"{'-' * 30}\n")
    except IOError:
        # Handle the case where the file cannot be opened
        print("Error opening file for writing.")

def saveAdminAppointmentsToFile():
    # Open a file named "admin_appointments.txt" for writing
    try:
        with open('admin_appointments.txt', 'w') as adminFile:
            for count in range(full_appointment_count):
                adminFile.write(f"Service: {full_appointment[count].service}\n"
                                f"Date:    {full_appointment[count].date}\n"
                                f"Time:    {full_appointment[count].time}\n"
                                f"Doctor:  {full_appointment[count].doctor}\n"
                                f"Name:    {full_appointment[count].name}\n"
                                f"Phone:   {full_appointment[count].phone}\n"
                                f"{'-' * 30}\n")
    except IOError:
        # Handle the case where the file cannot be opened
        print("Error opening admin appointments file for writing.\n")

def saveAdminAppointmentsToFile2():
    # Open a file named "admin_appointments.txt" for writing and reading ("w+") mode
    try:
        with open('admin_appointments.txt', 'w+') as adminFile:
            for count in range(full_appointment_count):
                adminFile.write(f"Service: {full_appointment[count].service}\n"
                                f"Date:    {full_appointment[count].date}\n"
                                f"Time:    {full_appointment[count].time}\n"
                                f"Doctor:  {full_appointment[count].doctor}\n"
                                f"Name:    {full_appointment[count].name}\n"
                                f"Phone:   {full_appointment[count].phone}\n"
                                f"{'-' * 30}\n")
    except IOError:
        print("\nError opening admin appointments file for writing.\n")

    adminFile.close()


def time_validation(date, time, doctor):
    # Check if the date, time and doctor of the new appointment mactch an existing appointment
    
    for count in range (full_appointment_count):
        
        # Check if the date matches
        if (date == full_appointment[count].date and time == full_appointment[count].time and doctor == full_appointment[count].doctor):
            return 0
    
    # If no existing appointment matches, return 1, indicating the time slot is available
    return 1

def timevalidation2(date,time,doctor,choice):
    # First, check if the new date, time, and doctor match the chosen appointment (specified by 'choice')
    if (date == schedule_list[choice].date and time == schedule_list[choice].time and doctor == schedule_list[choice].doctor):
        
        # The chosen appointment is being edited, so the same slot can be used
        return 1
    
    else:
        # If the new date, time, and doctor do not match the chosen appointment, iterate through all full_appointments to check for conflicts
        for count in range (full_appointment_count):
            if (date == full_appointment[count].date and time == full_appointment[count].time and doctor == full_appointment[count].doctor):
                
                # Time slot is already booked by another appointment
                return 0
    
    # If no conflicts were found, return 1, indicating the time slot is available
    return 1


def load_file():
    global appointment_count
    line_counter = 1
    # Create a file name based on the provided username
    file_name = f"{username}.txt"

    # Open the file for reading
    try:
        with open(file_name, "r") as file:
            # Initialize an appointment_count variable to keep track of loaded appointments

            for line in file:
                line_counter += 1
                # Read each line from the file and store its values in the schedule_list array
                values = line.strip().split(':')

                if len(values) >= 2:
                    field, data = values[0], values[1].strip()

                    if field == "Service":
                        schedule_list[appointment_count].service = data
                    elif field == "Date":
                        schedule_list[appointment_count].date = data
                    elif field == "Time":
                        schedule_list[appointment_count].time = data
                    elif field == "Doctor":
                        schedule_list[appointment_count].doctor = data
                    elif field == "Name":
                        schedule_list[appointment_count].name = data
                    elif field == "Phone":
                        schedule_list[appointment_count].phone = data
                    if line_counter % 7 == 0:
                        # A separator indicates the end of an appointment
                        appointment_count += 1

    except FileNotFoundError:
        # If the file cannot be opened (doesn't exist), simply return
        return

    file.close()


def loadAdminAppointmentsToFile():
    global full_appointment_count
    line_counter = 1
    try:
        # Open the "admin_appointments.txt" file for reading
        with open('admin_appointments.txt', 'r') as adminFile:
            # Initialize a counter to keep track of loaded admin appointments
        
            for line in adminFile:
                line_counter += 1
                # Read each line from the file and store its values in the full_appointment array
                values = line.strip().split(':')

                if len(values) >= 2:
                    field, data = values[0], values[1].strip()

                    if field == "Service":
                        full_appointment[full_appointment_count].service = data
                    elif field == "Date":
                        full_appointment[full_appointment_count].date = data
                    elif field == "Time":
                        full_appointment[full_appointment_count].time = data
                    elif field == "Doctor":
                        full_appointment[full_appointment_count].doctor = data
                    elif field == "Name":
                        full_appointment[full_appointment_count].name = data
                    elif field == "Phone":
                        full_appointment[full_appointment_count].phone = data
                    if line_counter % 7 == 0:
                        # A separator indicates the end of an appointment
                        full_appointment_count += 1

    except FileNotFoundError:
        return
    
    adminFile.close()


def selectDate():
    global date

    # The number of days to generate
    num_days = 7
    available_dates = show_available_dates(num_days)

    print("\nSelect a date: \n")

    # Print the formatted date strings
    for i, date_value in enumerate(available_dates):
        print("{}. {}\n".format(i+1, date_value))
    
    # Input validation loop for date choice
    while True:
        try: 
            choice_date = int(input("Enter your choice: "))

            if 1 <= choice_date <= 5:
                date = available_dates[choice_date - 1]
                return date
            else:
                print("Invalid selection. Re-enter your choice.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

        

def selectTime():
    global time 

    print("\nSelect a time:\n")
    print("1. 0800hrs\n")
    print("2. 0900hrs\n")
    print("3. 1000hrs\n")
    print("4. 1100hrs\n")
    print("5. 1400hrs\n")
    print("6. 1500hrs\n")
    print("7. 1600hrs\n")
    print("8. 1700hrs\n")

    # Input validation loop for time choice
    try:
        while True:
            choice_time = int(input("Enter your choice for time selection: "))

            if 1 <= choice_time <= 8:
                break
            else:
                choice_time = input("\nInvalid selection. Re-enter your choice: ")
    except ValueError:
        print("Invalid input. Please enter a valid input.") 

    # Map the user's choice to the corresponding time in "1800hrs" format
    time_mapping = {
        1: "0800hrs",
        2: "0900hrs",
        3: "1000hrs",
        4: "1100hrs",
        5: "1400hrs",
        6: "1500hrs",
        7: "1600hrs",
        8: "1700hrs",
    }
    time = time_mapping[choice_time]

    return time

def selectService():

    print("\n1. Outpatient Treatment")
    print("\n2. Quit Smoking Service")
    print("\n3. Pre-Marital Screening")
    print("\n4. Medical check up")
    print("\n5. Dental check up")

    # Input validation loop for service choice
    while (True):

        choice = int(input ("\n\nSelect a service : "))

        try: 

            if (choice >= 1 and choice <= 5 ):
                break
            else:
                print("\nInvalid selection. Re-enter your choice : ")
        except ValueError:
            print ("Invalid input. Please enter a number.")

    # Map the user's choice to the corresponding service
    if (choice == 1):
        service = "Outpatient Treatment"

    elif (choice == 2):
        service = "Quit Smoking Service"

    elif (choice == 3):
        service = "Pre-Marital Screening"

    elif (choice == 4):
        service = "Medical check up"

    elif (choice == 5):
        service = "Dental check up"
    
    return service

def selectDoctor(date, time):
    global choice_doc, choice_doc2, full_appointment, full_appointment_count

    doctor = ""
    doctors = ["Doctor Wee", "Doctor Lye", "Doctor Tan"]
    Max_doctors = 3
    doctorAvailable = True

    while True:
        choice_doc = getChoice_Doc()

        if choice_doc.lower() == 'y':
            print("\n1. Doctor Wee")
            print("2. Doctor Lye")
            print("3. Doctor Tan")

            try:
                choice_doc2 = int(input("Select the doctor you wish to book an appointment with: "))

                if 1 <= choice_doc2 <= 3:
                    doctor = doctors[choice_doc2 - 1]
                else:
                    print("\nInvalid selection. Please re-enter your choice.")
                    continue

                # Check if the selected doctor has any conflicting appointments
                doctorAvailable = True

                for count in range(full_appointment_count):
                    if (
                        full_appointment[count].date == date
                        and full_appointment[count].doctor == doctor
                        and full_appointment[count].time == time
                    ):
                        # The doctor is not available
                        doctorAvailable = False
                        break

                # Exit the loop whether the doctor is available or not available
                break

            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                continue

        elif choice_doc.lower() == 'n':
            for count in range(Max_doctors):
                doctorAlreadyBooked = any(
                    appt.date == date
                    and appt.time == time
                    and appt.doctor == doctors[count]
                    for appt in full_appointment
                )

                if not doctorAlreadyBooked:
                    doctor = doctors[count]
                    doctorAvailable = True
                    break

            # Exit the outer loop
            if doctorAvailable:
                break

        else:
            print("\nInvalid selection.")

    return doctor


def getChoice_Doc():
    choice_doc = input("\nDo you need a specific doctor? [Y|N]: ")
    return choice_doc
        
def show_available_dates(num_days):
    global weekday_names, month_names, SECONDS_PER_DAY
    SECONDS_PER_DAY = 86400
    current_time = datetime.now()

    # Skip the current day(today)
    current_time += timedelta(days=1)

    # Initialize an array to store datetime values
    datetime_values = []

    # Loop to generate datetime values for the next 7 days
    for _ in range(num_days):

        # Get the day of the week for the next day (0 = Monday, 1 = Tuesday, etc)
        next_day = current_time.weekday()

        # Check if the next day is not a weekend (0 = Sunday, 6 = Saturday)
        if next_day < 5:
            # Store the datetime value in the array
            datetime_values.append(current_time)

        # Calculate the timestamp for the next day
        current_time += timedelta(days=1)

    # Define an array of weekday names
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Define an array of months names
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Create an array of strings to store the formatted date strings
    formatted_dates = []

    # Format the date strings and store them in the array
    for date_value in datetime_values:
        formatted_date = date_value.strftime("%d %b %Y (%A)")
        formatted_dates.append(formatted_date)

    return formatted_dates


def username_validation():
    try:
        with open("user_details.txt", "r") as file1:
            for line in file1:
                if f"Username: {username}" in line:
                    return True
    except IOError:
        return False

    return False

def searchAppointments():
    print("\n=====================================================")
    print("\n\t\tSearch Appointments")
    print("\n=====================================================")

    print("1. Search by Service")
    print("2. Search by Date")
    print("3. Search by Time")
    print("4. Search by Doctor")
    print("5. Search by Name")
    print("6. Search by Phone")
    print("7. Back to Main Menu")

    # Input validation loop for search choice
    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= 7:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if choice == 1:
        # Search by Service
        searchByService()

    elif choice == 2:
        # Search by Date
        searchByDate()

    elif choice == 3:
        # Search by Time
        searchByTime()

    elif choice == 4:
        # Search by Doctor
        searchByDoctor()

    elif choice == 5:
        # Search by Name
        searchByName()

    elif choice == 6:
        # Search by Phone
        searchByPhone()

    elif choice == 7:
        # Return to the main menu
        display_user_home()

# Function to search for appointments by service
def searchByService():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Service")
    print("\n=========================================================\n")

    print("List of Services:")
    print("1. Outpatient Treatment")
    print("2. Quit Smoking Service")
    print("3. Pre-Marital Screening")
    print("4. Medical check up")
    print("5. Dental check up")

    # Input validation loop for service choice
    while True:
        try:
            service_choice = int(input("\nEnter the number corresponding to the service: "))

            if 1 <= service_choice <= 5:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Map the user's choice to the corresponding service
    services = [
        "Outpatient Treatment",
        "Quit Smoking Service",
        "Pre-Marital Screening",
        "Medical check up",
        "Dental check up"
    ]
    searchService = services[service_choice - 1]

    # Filter appointments that match the search service
    matching_appointments = [appointment for appointment in schedule_list if appointment.service and appointment.service.lower() == searchService.lower()]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
    else:
        print(f"\nNo appointments found for the service: {searchService}.\n")

    # Return to the main menu
    searchAppointments()


# Function to search for appointments by date
def searchByDate():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Date")
    print("\n=========================================================\n")

    searchDate = input("\nEnter the date to search for (e.g., 25 Dec 2023): ")

    # Convert the entered date to the format used in appointments
    try:
        searchDate = datetime.strptime(searchDate, "%d %b %Y").strftime("%d %b %Y")
    except ValueError:
        print("Invalid date format. Please use the format (e.g., 25 Dec 2023).")
        return

    # Iterate through appointments
    for appointment in schedule_list:
        # Check if the date attribute is not None
        if appointment.date:
            # Extract the date from the appointment, including the day of the week
            appointment_date_with_day = appointment.date
            # Try to parse the day of the week and remove it
            try:
                appointment_date = datetime.strptime(appointment_date_with_day, "%d %b %Y (%A)").strftime("%d %b %Y")
            except ValueError:
                # If parsing fails, assume the date format without the day of the week
                appointment_date = datetime.strptime(appointment_date_with_day, "%d %b %Y").strftime("%d %b %Y")

            if appointment_date == searchDate:
                # Accumulate matching appointments
                found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print(f"\nAppointments for the date: {searchDate}")
        displayAppointments(found_appointments)
    else:
        print("\nNo appointments found for the given date.\n")

    # Return to the main menu
    searchAppointments()

# Function to search for appointments by time
def searchByTime():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Time")
    print("\n=========================================================\n")

    searchTime = input("\nEnter the time to search for: ")

    # Iterate through appointments
    for appointment in schedule_list:
        if appointment.time == searchTime:
            # Accumulate matching appointments
            found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print("\nAppointments for the given time:")
        displayAppointments(found_appointments)
    else:
        print("No appointments found for the given time.\n")

    # Return to the main menu or perform any other desired action
    searchAppointments()


# Function to search for appointments by doctor
def searchByDoctor():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Doctor")
    print("\n=========================================================\n")

    # Display the list of doctors
    print("List of Doctors:")
    print("1. Doctor Wee")
    print("2. Doctor Lye")
    print("3. Doctor Tan")

    # Input validation loop for doctor choice
    while True:
        try:
            doctor_choice = int(input("\nEnter the number corresponding to the doctor: "))

            if 1 <= doctor_choice <= 3:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Map the user's choice to the corresponding doctor
    doctors = ["Doctor Wee", "Doctor Lye", "Doctor Tan"]
    searchDoctor = doctors[doctor_choice - 1]

    # Iterate through appointments
    for appointment in schedule_list:
        if appointment.doctor == searchDoctor:
            # Accumulate matching appointments
            found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print(f"\nAppointments for {searchDoctor}:")
        displayAppointments(found_appointments)
    else:
        print(f"\nNo appointments found for {searchDoctor}.\n")

    # Return to the main menu or perform any other desired action
    searchAppointments()

# Function to search for appointments by name
def searchByName():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Name")
    print("\n=========================================================\n")

    searchName = input("\nEnter the name to search for: ")

    # Iterate through appointments
    for appointment in schedule_list:
        if appointment.name and appointment.name.lower() == searchName.lower():
            # Check if the name attribute is not None before using lower()
            found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print(f"\nAppointments for {searchName}:")
        displayAppointments(found_appointments)
    else:
        print("\nNo appointments found for the given name.\n")

    # Return to the main menu or perform any other desired action
    searchAppointments()


def searchByPhone():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Phone number")
    print("\n=========================================================\n")

    searchPhone = input("\nEnter the Phone number to search for: ")

    # Iterate through appointments
    for appointment in schedule_list:
        if appointment.phone == searchPhone:
            # Accumulate matching appointments
            found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print(f"\nAppointments for the given phone number ({searchPhone}):")
        displayAppointments(found_appointments)
    else:
        print("\nNo appointments found for the given phone number.\n")

    # Return to the main menu or perform any other desired action
    searchAppointments()

def addUserAppointment():
    global username, appointment_count
    print("\n=========================================================")
    print("\n\t\tAdd Appointment for User")
    print("\n=========================================================\n")
    username = input("Enter user's username: ")

    # Validate if the username exists

    if not username_validation():
        print("The username is not found")
        return
    appointment_count = 0
    load_file()
    addAppointment()

def editUserAppointment():
    global username, appointment_count
    print("\n=========================================================")
    print("\n\t\tEdit Appointment for User")
    print("\n=========================================================\n")
    username = input("Enter user's username: ")

    # Validate if the username exists

    if not username_validation():
        print("The username is not found")
        return
    appointment_count = 0
    load_file()
    editAppointment()

def deleteUserAppointment():
    global username, appointment_count
    print("\n=========================================================")
    print("\n\t\tDelete Appointment for User")
    print("\n=========================================================\n")
    username = input("Enter user's username: ")

    # Validate if the username exists

    if not username_validation():
        print("The username is not found")
        return
    appointment_count = 0
    load_file()
    deleteAppointment()

def viewUserAppointment():
    global username, appointment_count
    print("\n=========================================================")
    print("\n\t\tView User Appointment")
    print("\n=========================================================\n")
    username = input("Enter user's username: ")

    # Validate if the username exists

    if not username_validation():
        print("The username is not found")
        return
    appointment_count = 0
    load_file()
    viewAppointment()
    
def searchAllAppointments():
    print("\n====================================================================================================================================")
    print("\n\t\t\t\t\t\tSearch All Appointments")
    print("\n====================================================================================================================================")

    print("1. Search by Service")
    print("2. Search by Date")
    print("3. Search by Time")
    print("4. Search by Doctor")
    print("5. Search by Name")
    print("6. Search by Phone")
    print("7. Back to Main Menu")

    # Input validation loop for search choice
    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= 7:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if choice == 1:
        # Search by Service
        searchAllByService()

    elif choice == 2:
        # Search by Date
        searchAllByDate()

    elif choice == 3:
        # Search by Time
        searchAllByTime()

    elif choice == 4:
        # Search by Doctor
        searchAllByDoctor()

    elif choice == 5:
        # Search by Name
        searchAllByName()

    elif choice == 6:
        # Search by Phone
        searchAllByPhone()

    elif choice == 7:
        # Return to the main menu
        display_admin_home()

def searchAllByService():
    found = 0

    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Service")
    print("\n=========================================================\n")

    print("List of Services:")
    print("1. Outpatient Treatment")
    print("2. Quit Smoking Service")
    print("3. Pre-Marital Screening")
    print("4. Medical check up")
    print("5. Dental check up")

    # Input validation loop for service choice
    while True:
        try:
            service_choice = int(input("\nEnter the number corresponding to the service: "))

            if 1 <= service_choice <= 5:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Map the user's choice to the corresponding service
    services = [
        "Outpatient Treatment",
        "Quit Smoking Service",
        "Pre-Marital Screening",
        "Medical check up",
        "Dental check up"
    ]
    searchService = services[service_choice - 1]

    # Filter appointments that match the search service
    matching_appointments = [appointment for appointment in full_appointment if appointment.service and appointment.service.lower() == searchService.lower()]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
        found = 1

    if not found:
        print(f"\nNo appointments found for the service: {searchService}.\n")

    # Return to the main menu
    searchAllAppointments()

def searchAllByDate():
    found_appointments = []

    print("\n=========================================================")
    print("\n\t\tSearch Appointments by Date")
    print("\n=========================================================\n")

    searchDate = input("\nEnter the date to search for (e.g., 25 Dec 2023): ")

    # Convert the entered date to the format used in appointments
    try:
        searchDate = datetime.strptime(searchDate, "%d %b %Y").strftime("%d %b %Y")
    except ValueError:
        print("Invalid date format. Please use the format (e.g., 25 Dec 2023).")
        return

    # Iterate through appointments
    for appointment in full_appointment:
        # Check if the date attribute is not None
        if appointment.date:
            # Extract the date from the appointment, including the day of the week
            appointment_date_with_day = appointment.date
            # Try to parse the day of the week and remove it
            try:
                appointment_date = datetime.strptime(appointment_date_with_day, "%d %b %Y (%A)").strftime("%d %b %Y")
            except ValueError:
                # If parsing fails, assume the date format without the day of the week
                appointment_date = datetime.strptime(appointment_date_with_day, "%d %b %Y").strftime("%d %b %Y")

            if appointment_date == searchDate:
                # Accumulate matching appointments
                found_appointments.append(appointment)

    if found_appointments:
        # Display all matching appointments
        print(f"\nAppointments for the date: {searchDate}")
        displayAppointments(found_appointments)
    else:
        print("\nNo appointments found for the given date.\n")

    # Return to the main menu
    searchAllAppointments()


def searchAllByTime():
    found = 0

    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Time")
    print("\n=========================================================\n")

    searchTime = input("\nEnter the time to search for (e.g., 0800hrs): ")

    # Filter appointments that match the search time
    matching_appointments = [appointment for appointment in full_appointment if appointment.time == searchTime]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
        found = 1

    if not found:
        print("\nNo appointments found for the given time.\n")

    # Return to the main menu
    searchAllAppointments()

def searchAllByDoctor():
    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Doctor")
    print("\n=========================================================\n")

    # Display the list of available doctors
    print("List of Doctors:")
    for index, doctor in enumerate(["Doctor Wee", "Doctor Lye", "Doctor Tan"], start=1):
        print(f"{index}. {doctor}")

    # Input validation loop for doctor choice
    while True:
        try:
            doctor_choice = int(input("\nEnter the number corresponding to the doctor: "))

            if 1 <= doctor_choice <= 3:
                break
            else:
                print("Invalid selection. Re-enter your choice.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Map the user's choice to the corresponding doctor
    doctors = ["Doctor Wee", "Doctor Lye", "Doctor Tan"]
    searchDoctor = doctors[doctor_choice - 1]

    # Filter appointments that match the search doctor
    matching_appointments = [appointment for appointment in full_appointment if appointment.doctor and appointment.doctor.lower() == searchDoctor.lower()]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
    else:
        print(f"\nNo appointments found for {searchDoctor}.\n")

    # Return to the main menu
    searchAllAppointments()

def searchAllByName():
    found = 0

    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Name")
    print("\n=========================================================\n")

    searchName = input("\nEnter the patient's name to search for: ")

    # Filter appointments that match the search name
    matching_appointments = [appointment for appointment in full_appointment if appointment.name and appointment.name.lower() == searchName.lower()]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
        found = 1

    if not found:
        print("\nNo appointments found for the given name.\n")

    # Return to the main menu
    searchAllAppointments()

def searchAllByPhone():
    found = 0

    print("\n=========================================================")
    print("\n\t\tSearch All Appointments by Phone Number")
    print("\n=========================================================\n")

    searchPhone = input("\nEnter the phone number to search for: ")

    # Filter appointments that match the search phone number
    matching_appointments = [appointment for appointment in full_appointment if appointment.phone == searchPhone]

    if matching_appointments:
        # Sort the matching_appointments list by date
        matching_appointments.sort(key=lambda x: (x.date or ''))

        # Call the display function to print the matching appointments
        displayAppointments(matching_appointments)
        found = 1

    if not found:
        print("\nNo appointments found for the given phone number.\n")

    # Return to the main menu
    searchAllAppointments()


def displayAppointments(appointments):
    # Print the header
    print("\n------------------------------------------------------------------------------------------------------------------------------------")
    print("\n| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format("No.", "Date", "Time", "Service", "Doctor", "Name", "Phone Number"))
    print("\n------------------------------------------------------------------------------------------------------------------------------------")

    # Loop through and display each appointment
    for count, appointment in enumerate(appointments, start=1):
        print("| {:<3} | {:<23} | {:<11} | {:<21} | {:<10} | {:<30} | {:<12} |".format(
            count, appointment.date, appointment.time, appointment.service,
            appointment.doctor, appointment.name, appointment.phone))

    
    print("====================================================================================================================================\n")

def getname():
    return input("\nEnter your name: ")

def getphone():
    return input("\nEnter your phone number: ")

if __name__ == "__main__":
   # full_appointment = []
    home()
