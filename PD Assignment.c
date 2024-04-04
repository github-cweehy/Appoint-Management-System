#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#define max_appointment 100
#define MAX_DOCTORS 3

char username[25], password[25];
int appointment_count = 0;
int full_appointment_count = 0;
int count = 0;
char code[20];

// Define a structure for appointment scheduling
struct schedule
{
	char date[99];
	char time[99];
	char service[99];
	char name[99];
	char phone[99];
	char doctor[99];
} schedule_list[max_appointment],new_appointment, full_appointment[max_appointment];

// Function prototypes
void home();
void reg();
void login();
void adminLogin();
void display_user_home();
void display_admin_home();
void saveAppointmentsToFile();
void saveAppointmentsToFile2();
void saveAdminAppointmentsToFile();
void saveAdminAppointmentsToFile2();
int time_validation(const char *date, const char *time, const char *doctor);
int time_validation2(const char *date,const char *time, const char *doctor,int choice);
void load_file(const char*username);
void addAppointment();
void editAppointment(char choice_doc);
void deleteAppointment();
int selectDoctor(char doctor[99], const char schedule_list[MAX_DOCTORS][50], int appointment_count, const char date[99], const char time[99]);
void selectService(char service[99]);
void selectDate(char date[99]);
void selectTime(char time[99]);
void loadAdminAppointmentsToFile();
char** show_available_dates(int num_days);
void viewAppointment();
void viewAllAppointment();
int username_validation(const char *username);
void searchAppointmentsByName();
void searchAppointmentsByContact();
void searchAppointmentsByService();
void searchAppointmentsByDate();
void searchAppointmentsByTime();
void searchAllAppointmentsByName();

int main()
{
	home();
	return 0;
}

// Function for the main menu
void home()
{
	int choice;
	
	//system("cls");
	printf("============================================================");
	printf("\n\t\tWELCOME TO Harry Potter");
	printf("\n============================================================");
	
	printf("\n\n1. REGISTER\n2. LOGIN\n3. ADMIN LOGIN\n4. Exit");
	
	fflush(stdin);
	printf("\n\nEnter your choice: ");
	scanf("%d",&choice);
	// Use a loop to handle user's choice
	while(choice)
	{
		if(choice == 1)
		{
			reg();
			break;
		}
		else if(choice == 2)
		{
			login();
			break;
			
		}
		else if(choice == 3)
		{
			adminLogin();
			break;
		}
		else if(choice == 4)
		{
			exit(0);
		}
		else
		{
			fflush(stdin);
			printf("\n\nInvalid choice, please re-enter your choice: ");
			scanf("%d",&choice);
		}
	}
}


// Function for user registration
void reg()
{
	char login_status, select;
	int len_username, len_password,count;
	system("cls");
	printf("============================================================");
	printf("\n\t\tRegister Account");
	printf("\n============================================================");
	
	while(1)
	{
	// prompt username and password
		fflush(stdin);
		printf("\n\nEnter username (Must between 5 characters to 10 characters) : ");
		gets(username);
		//check for duplicate username
		if(username_validation(username))
		{
			printf("\nUsername is already taken. Please choose another username.");
			continue;
		}
		printf("Enter password (Must between 5 characters to 10 characters) : ");
		gets(password);
		
		len_username = strlen(username);
		len_password = strlen(password);
		
		// validate the length of username and password
		if (len_username <= 4 || len_username > 10 )
		{
			// username must be more than 5 characters
			printf("\nUsername must between 5 characters to 10 characters ");
		}
		
		if (len_password <= 4 || len_password > 10)
		{
			// password must be more than 5 characters
			printf("\nPassword must between 5 characters to 10 characters ");
		}
		// If both username and password are within valid ranges, exit the loop
		if (len_password > 4 && len_username>4 && len_username<=10 && len_password<=10)
		{
			break;
		}
	}
	// Open a file for writing user details
	FILE *file1 = fopen("user_details.txt", "a+");
	    if (file1 == NULL) 
		{
	        printf("Error opening file for writing.\n");
	        return;
	    }
	    // Write the username and password to the file
	    fprintf(file1, "%s\n%s\n", username,password);
	    fclose(file1);
	    printf("\nRegister successfully!");
	
	// Prompt the user to login or return to the home menu
	while(login_status != 'Y' && login_status != 'y' && login_status != 'N' && login_status != 'n')
	{
		fflush(stdin);
		printf("\nLogin now? [Y|N]: ");
		scanf("%c", &login_status);
		if(login_status == 'Y' || login_status == 'y')
		{
			login();
		}
		else if(login_status == 'N'|| login_status == 'n')
		{
			home();
		}
		else
		{	
			printf("\nInvalid selection.\n");
		}
	}
}

// Function for user login
void login()
{
	char entered_username[25], entered_password[25];
	static char user_id[25];
	int true = 0;
	system("cls");
	printf("============================================================");
	printf("\n\t\t\tLogin");
	printf("\n============================================================");
	
	// prompt username and password 
	while(1)
	{
		fflush(stdin);
		printf("\nEnter username : ");
		gets(entered_username);
		printf("Enter password : ");
		gets(entered_password);
	
		// Verify username and password against stored user details in a file
		FILE *file1 = fopen("user_details.txt", "r");
		if (file1 == NULL)
		{
			printf("\nError opening file for reading.");
	        return;
		}
		// Loop through the file to check each user's details
		while (!feof(file1))
   		{
	        fscanf(file1, "%s%s", username, password);
	
	        // Compare entered_username and entered_password with file_username and file_password
	        if (strcmp(entered_username, username) == 0 && strcmp(entered_password, password) == 0)
	        {
	            true = 1; // User found
	            break;     // Exit the loop
	        }
    }

    fclose(file1);

    if (true)
    {
        printf("\nLogin successful\n");
        load_file(username); //Load user appointment details
        loadAdminAppointmentsToFile(); //Load admin appointments
        display_user_home();
    }
    else
    {
        printf("\nThe username or password you entered is incorrect. Please try again.\n"); 
    }
	}

}

// Function for admin login
void adminLogin()
{
	int i=0;
	// Continue looping until a valid admin ID is entered or the user chooses to go back to the home menu
	while(i<1)
	{
		fflush(stdin);
		printf("\nYour admin ID : ");
		gets(code);
		
		// Check if the entered code matches one of the valid admin IDs
		if(strcmp(code,"1221204416") == 0 || strcmp(code,"1221205257") == 0 || strcmp(code,"1221204572") == 0)
		{
			i++; // Set i to 1 to exit the loop
	        loadAdminAppointmentsToFile(); // Load admin appointments data
	        display_admin_home(); // Display the user's home menu
		}
		else if(strcmp(code,"B") == 0 || strcmp(code,"b") == 0)
		{
			i++; // Set i to 1 to exit the loop
			home(); // Go back to the home menu
		}
		else
		{
			// Display an error message for an incorrect admin ID and allow the user to try again
			printf("\nWrong ID. Please try again. (Enter B back to home)\n");
		}
	}
	
}

// Function to display the user's home screen
void display_user_home() 
{
    char choice2, choice_doc;
    int displayMenu = 1; // Flag to control menu display

    while (1) 
	{
        if (displayMenu) 
		{
            // Display the menu options to the user
            printf("\n=========================================================");
            printf("\n\t\tMenu Selection");
            printf("\n=========================================================");
            printf("\n1. Add Appointment");
            printf("\n2. Edit Apointment");
            printf("\n3. Delete/Cancel Appointment");
            printf("\n4. View Appointment");
            printf("\n5. Search Appointments by Name");
            printf("\n6. Search Appointments by Contact");
            printf("\n7. Logout");
            printf("\n8. Exit");  
        }
        fflush(stdin);
        printf("\n\nEnter your choice : ");
        scanf("%c", &choice2); 

        switch (choice2) 
		{
            case '1':
                addAppointment(); // Call a function to add a new appointment
                break;
            case '2':
                editAppointment(choice_doc); // Call a function to edit an existing appointment
                break;
            case '3':
                deleteAppointment(); // Call a function to delete/cancel an appointment
                break;
            case '4':
                viewAppointment(); // Call a function to view appointments (user)
                break;
            case '5':      
                searchAppointmentsByName(); // Call a function to view appointments (user)
                break;
            case '6':
            	searchAppointmentsByContact();
            	break; 
            case '7':
                appointment_count = 0; // Reset schedule count
                full_appointment_count = 0; // Reset admin schedule count
                strcpy(code, ""); // Clear the admin code
                home(); // Go back to the home menu
                break;
            case '8':
            	exit(0); // Exit the program
            default:
                printf("\nInvalid selection! Please enter a valid choice.\n");
                displayMenu = 0; // Do not display the menu on invalid selection
        }

        if (choice2 >= '1' && choice2 <= '7') 
		{
            displayMenu = 1; // Display the menu on valid selections
        }
    }
}

void display_admin_home() 
{
    char choice2, choice_doc;
    int displayMenu = 1; // Flag to control menu display

    while (1) 
	{
        if (displayMenu) 
		{
            // Display the menu options to the user
            printf("\n=========================================================");
            printf("\n\t\tMenu Selection");
            printf("\n=========================================================");
            printf("\n1. View Appointment");
            printf("\n2. Search Appointments by Name");
            printf("\n3. Logout");
            printf("\n4. Exit");  
        }
        fflush(stdin);
        printf("\n\nEnter your choice : ");
        scanf("%c", &choice2); 

        switch (choice2) 
		{
            case '1':
                viewAllAppointment(); // Call a function to view all appointments (admin)
                break;
            case '2':
                searchAllAppointmentsByName(); // Call a function to view all appointments (admin)
                break;
            case '3':
                appointment_count = 0; // Reset schedule count
                full_appointment_count = 0; // Reset admin schedule count
                strcpy(code, ""); // Clear the admin code
                home(); // Go back to the home menu
                break;
            case '4':
                exit(0); // Exit the program
                break;
            default:
                printf("\nInvalid selection! Please enter a valid choice.\n");
                displayMenu = 0; // Do not display the menu on invalid selection
        }

        if (choice2 >= '1' && choice2 <= '4') 
		{
            displayMenu = 1; // Display the menu on valid selections
        }
    }
}

void addAppointment() 
{
    char date[99], time[99], service[99], doctor[99],name[99],phone[99], confirm;
    const char doctors[MAX_DOCTORS][50] = {"Doctor Wee", "Doctor Lye", "Doctor Tan"};

	// Function to select the desired medical service for the appointment
    selectService(service);
    
    // Function to select the appointment date
    selectDate(date);
    
    // Function to select the appointment time
    selectTime(time);
    
    // Function to select the doctor for the appointment
    selectDoctor(doctor, doctors, appointment_count, date, time);

	// Validate if the selected appointment time is available and doctor is selected
	if (time_validation(date,time,doctor) && strlen(doctor) > 1) 
	{
		fflush(stdin);
        printf("\nEnter your name : ");
        gets(name);
        printf("\nEnter your phone number : ");
        gets(phone);
        
        printf("\nDate               : %s",date);
        printf("\nTime               : %s",time);
        printf("\nService            : %s",service);
        printf("\nDoctor             : %s",doctor);
        printf("\nYour name          : %s",name);
        printf("\nYour phone number  : %s",phone);
        printf("\n\nAppointment confirmation [Y|N] : ");
        scanf("%c",&confirm);
        if(confirm == 'Y' || confirm == 'y')
        {
        	printf("");
		}
		else
		{
			printf("\nNo appointment was schedule.");
			display_user_home();
		}
        
        
        
        // Copy the appointment details into a new appointment structure
		strcpy(new_appointment.service, service);
        strcpy(new_appointment.date, date);
        strcpy(new_appointment.time, time);
        strcpy(new_appointment.doctor, doctor);
        strcpy(new_appointment.name, name);
        strcpy(new_appointment.phone, phone);
        
        // Check if the maximum appointment limit has been reached
        if (appointment_count < max_appointment) 
		{
			// Add the new appointment to the schedule list
            schedule_list[appointment_count++] = new_appointment;
            
            // Add the new appointment to the full appointment list
            full_appointment[full_appointment_count++] = new_appointment;
            
            // Save the updated appointments to a file
            saveAppointmentsToFile(); 
            saveAdminAppointmentsToFile();
            printf("\nAppointment scheduled successfully.\n");
        } 
		else 
		{
            printf("Maximum appointment limit reached. Cannot schedule.\n");
        }
    }
	else 
	{
		printf("\nThe selected time slot is fully booked or the doctor is not available. Please choose another time or doctor.\n");
    }
}

void editAppointment(char choice_doc)
{
	char date[99], time[99], service[99], doctor[99],name[99],phone[99],confirm;
	const char doctors[MAX_DOCTORS][50] = {"Doctor Wee", "Doctor Lye", "Doctor Tan"};
	int choice;
    printf("\n======================================");
    printf("\n\tEdit Appointment");
    printf("\n======================================");
	
    if (appointment_count > 0) 
	{
		// Display the user's appointments
		printf("\nYour Appointments:\n");
    	viewAppointment();
        printf("\nEnter the number of the appointment you want to edit (1 to %d): ", appointment_count);
        scanf("%d", &choice);

        // Validate the user's choice
        if (choice >= 1 && choice <= appointment_count) 
		{
            // Adjust the choice to match the array index
            choice--;
            // Prompt the user to select new service, date, time, and doctor
            selectService(service);
   	 		selectDate(date);
   			selectTime(time);
   			choice_doc = selectDoctor(doctor,doctors,appointment_count,date,time);
   			
   			if(choice_doc == 'N' || choice_doc == 'n')
   			{
   				strcpy(doctor,schedule_list[choice].doctor);
			}
   			
   			 // Check if the new time slot is valid and available
   			if(time_validation2(date,time,doctor,choice))
			{
				fflush(stdin);
		        printf("\nEnter your name : ");
		        gets(name);
		        printf("\nEnter your phone number : ");
		        gets(phone);
		        printf("\nDate               : %s",date);
		        printf("\nTime               : %s",time);
		        printf("\nService            : %s",service);
		        printf("\nDoctor             : %s",doctor);
		        printf("\nYour name          : %s",name);
		        printf("\nYour phone number  : %s",phone);
		        fflush(stdin);
		        printf("\n\nAppointment confirmation [Y|N] : ");
		        scanf("%c",&confirm);
		        if(confirm == 'Y' || confirm == 'y')
		        {
		        	printf("");
				}
				else
				{
					printf("\nNo appointment was edit.");
					display_user_home();
				}
		        
		        // Update the appointment details
				strcpy(new_appointment.service, service);
		        strcpy(new_appointment.date, date);
		        strcpy(new_appointment.time, time);
		        strcpy(new_appointment.doctor, doctor);
		        strcpy(new_appointment.name, name);
		        strcpy(new_appointment.phone, phone);
		        
		        if (full_appointment_count < max_appointment) 
				{
					// Update the appointment in both schedule_list and full_appointment
		            for(count = 0; count < full_appointment_count; count++)
		            {
		            	if(strcmp(schedule_list[choice].date,full_appointment[count].date) == 0 && 
						strcmp(schedule_list[choice].time,full_appointment[count].time) == 0 && 
						strcmp(schedule_list[choice].doctor,full_appointment[count].doctor) == 0)
		            	{
		            		full_appointment[count] = new_appointment;
		            		schedule_list[choice] = new_appointment;
						}
					}
		            // Save appointments to file after editing
		            saveAppointmentsToFile2(); 
		            saveAdminAppointmentsToFile2();
		            printf("\nAppointment scheduled successfully.\n");
		        } 
				else 
				{
		            printf("Maximum appointment limit reached. Cannot schedule.\n");
		        }
		        
			}
			else 
			{
				// The slot is already booked
				printf("\nThe selected time slot is already booked. Failed to edit appointment.\n");
		    }
    	}
    	else
    	{
    		printf("\nInvalid appointment number. Please select a valid appointment to edit.\n");
		}
	}
	else
	{
		printf("\n     No appointments to edit.\n\n");
		
	}
}

void deleteAppointment() 
{
    int choice;
    printf("\n======================================");
    printf("\n\tDelete Appointment");
    printf("\n======================================");

    // Display the user's appointments
    if (appointment_count > 0) 
	{
		printf("\nYour Appointments:\n");
   		viewAppointment();
		// Ask the user for the appointment number they want to delete
        printf("\nEnter the number of the appointment you want to delete (1 to %d): ", appointment_count);
        scanf("%d", &choice);

        // Validate the user's choice
        if (choice >= 1 && choice <= appointment_count) 
		{
            // Adjust the choice to match the array index
            choice--;

            // Shift the remaining appointments to fill the gap left by the deleted appointment
            for (count = choice; count < appointment_count - 1; count++) 
			{
                schedule_list[count] = schedule_list[count + 1];
            }
            appointment_count--;
            
            for (count = choice; count < full_appointment_count - 1; count++) 
			{
                full_appointment[count] = full_appointment[count + 1];
            }
            full_appointment_count--;

            // Save appointments to file after deleting
            saveAppointmentsToFile();
            saveAdminAppointmentsToFile();
			
			// Display a confirmation message
            printf("\nAppointment has been deleted/cancelled.\n");
        } 
		else 
		{
			// Display an error message for an invalid choice
            printf("\nInvalid choice.\n");
        }
    } 
	else 
	{
		// Display a message when there are no appointments to delete
        printf("\nNo appointments to delete.\n");
    }
}

void viewAppointment()
{
    printf("\n====================================================================================================================================");
    printf("\n\t\t\t\t\t\tAppointment Schedule");
    printf("\n====================================================================================================================================");
    
    if (appointment_count != 0) {
        printf("\n| %-3s | %-23s | %-11s | %-21s | %-10s | %-30s | %-12s |", "No.", "Date", "Time", "Service", "Doctor", "Name", "Phone Number");
        printf("\n------------------------------------------------------------------------------------------------------------------------------------");
        // Loop through and display each appointment
        for (count = 0; count < appointment_count; count++)
		{
        	printf("\n| %-3d | %-23s | %-11s | %-21s | %-10s | %-30s | %-12s |", count + 1, schedule_list[count].date,schedule_list[count].time,
        	schedule_list[count].service, schedule_list[count].doctor,schedule_list[count].name, schedule_list[count].phone);
        }
        printf("\n====================================================================================================================================\n");
    } 
	else 
	{
		// Display a message when there are no appointments
        printf("\n| %-102s |", "No record found.");
        printf("\n====================================================================================================================================\n");
    }
}

void viewAllAppointment()
{
    printf("\n====================================================================================================================================");
    printf("\n\t\t\t\t\t\tAppointment Schedule");
    printf("\n====================================================================================================================================");
    
    if (full_appointment_count != 0) 
	{
        printf("\n| %-3s | %-23s | %-11s | %-21s | %-10s | %-30s | %-12s |", "No.", "Date", "Time", "Service", "Doctor", "Name", "Phone Number");
        printf("\n------------------------------------------------------------------------------------------------------------------------------------");
        // Loop through and display each appointment in the full appointment list
        for (count = 0; count < full_appointment_count; count++)
		{
        	printf("\n| %-3d | %-23s | %-11s | %-21s | %-10s | %-30s | %-12s |", count + 1, full_appointment[count].date,full_appointment[count].time,
        	full_appointment[count].service, full_appointment[count].doctor,full_appointment[count].name, full_appointment[count].phone);
        }
        printf("\n====================================================================================================================================\n");
    } 
	else 
	{
		// Display a message when there are no appointments in the full appointment list
        printf("\n| %-102s |", "No record found.");
        printf("\n====================================================================================================================================\n");
    }
}

void saveAppointmentsToFile() 
{
	char file_name[100];
	// Create a file name based on the user's username
	sprintf(file_name,"%s.txt",username);
	
	// Open the file for writing
    FILE *file = fopen(file_name, "w");
    if (file == NULL) 
	{
		// Handle the case where the file cannot be opened
        printf("Error opening file for writing.\n");
        return;
    }
	
	// Loop through each appointment and write its details to the file
	for (count = 0; count < appointment_count; count++) 
	{
        fprintf(file, "%s,%s,%s,%s,%s,%s\n", schedule_list[count].service, schedule_list[count].date, schedule_list[count].time, 
				schedule_list[count].doctor, schedule_list[count].name, schedule_list[count].phone);
    }
   	// Close the file when done writing
	fclose(file);
}

void saveAppointmentsToFile2() 
{
	char file_name[100];
	sprintf(file_name,"%s.txt",username);
	
	// Open the file for writing and reading ("w+" mode)
    FILE *file = fopen(file_name, "w+");
    if (file == NULL) 
	{
        printf("Error opening file for writing.\n");
        return;
    }
	
	for (count = 0; count < appointment_count; count++) 
	{
        fprintf(file, "%s,%s,%s,%s,%s,%s\n", schedule_list[count].service, schedule_list[count].date, schedule_list[count].time, 
				schedule_list[count].doctor, schedule_list[count].name, schedule_list[count].phone);
    }
    
   
    fclose(file);
}

void saveAdminAppointmentsToFile() 
{
	// Open a file named "admin_appointments.txt" for writing
    FILE *adminFile = fopen("admin_appointments.txt", "w");
    if (adminFile == NULL) 
	{
        printf("Error opening admin appointments file for writing.\n");
        return;
    }

    for (count = 0; count < full_appointment_count; count++) {
        fprintf(adminFile, "%s,%s,%s,%s,%s,%s\n", full_appointment[count].service,
                full_appointment[count].date, full_appointment[count].time, full_appointment[count].doctor,
                full_appointment[count].name, full_appointment[count].phone);
    }

    fclose(adminFile);
}

void saveAdminAppointmentsToFile2() 
{
	// Open a file named "admin_appointments.txt" for writing and reading ("w+") mode
    FILE *adminFile = fopen("admin_appointments.txt", "w+");
    if (adminFile == NULL) 
	{
        printf("Error opening admin appointments file for writing.\n");
        return;
    }

    for (count = 0; count < full_appointment_count; count++) {
        fprintf(adminFile, "%s,%s,%s,%s,%s,%s\n", full_appointment[count].service,
                full_appointment[count].date, full_appointment[count].time, full_appointment[count].doctor,
                full_appointment[count].name, full_appointment[count].phone);
    }

    fclose(adminFile);
}

int time_validation(const char *date,const char *time, const char * doctor)
{
	// Check if the date, time, and doctor of the new appointment match an existing appointment
	for (count = 0; count < full_appointment_count; count++)
	{
        // Check count the date matches
        if (strcmp(date, full_appointment[count].date) == 0 && strcmp(time, full_appointment[count].time) == 0 && strcmp(doctor, full_appointment[count].doctor) == 0 )
		{
			return 0; // Time slot is already booked	
        }
    }
    // If no existing appointment matches, return 1, indicating the time slot is available
    return 1;
}

int time_validation2(const char *date,const char *time, const char * doctor,int choice)
{
	// First, check if the new date, time, and doctor match the chosen appointment (specified by 'choice')
	if(strcmp(date,schedule_list[choice].date) == 0 && strcmp(time,schedule_list[choice].time) == 0 && strcmp(doctor,schedule_list[choice].doctor) == 0)
	{
		return 1; // The chosen appointment is being edited, so the same slot can be used
	}
	else
	{
		// If the new date, time, and doctor do not match the chosen appointment, iterate through all full_appointments to check for conflicts
		for(count=0;count<full_appointment_count;count++)
		{
			if(strcmp(date,full_appointment[count].date) == 0 && strcmp(time,full_appointment[count].time) == 0 && strcmp(doctor,full_appointment[count].doctor) == 0)
			{
				return 0; // Time slot is already booked by another appointment
			}
		}
		return 1;  // If no conflicts were found, return 1, indicating the time slot is available
	}
}

void load_file(const char *username)
{
	
    char file_name[100];
    // Create a file name based on the provided username
    sprintf(file_name, "%s.txt", username);
    // Open the file for reading
    FILE *file = fopen(file_name, "r");

    if (file == NULL)
    {
        return; // If the file cannot be opened (doesn't exist), simply return
    }
	// Initialize an appointment_count variable to keep track of loaded appointments
    while (fscanf(file, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^\n]\n",
                  schedule_list[appointment_count].service, schedule_list[appointment_count].date,
                  schedule_list[appointment_count].time, schedule_list[appointment_count].doctor,
                  schedule_list[appointment_count].name, schedule_list[appointment_count].phone) == 6)
    {
    	// Read each line from the file and store its values in the schedule_list array
        // Increase the appointment_count for each successfully loaded appointment
        appointment_count++;
    }
	// Close the file after reading
    fclose(file);
}

void loadAdminAppointmentsToFile() 
{
	// Open the "admin_appointments.txt" file for reading
    FILE *adminFile = fopen("admin_appointments.txt", "r");
    if (adminFile == NULL) 
	{
        return;
    }
    // Initialize a counter to keep track of loaded admin appointments
	while (fscanf(adminFile, "%[^,],%[^,],%[^,],%[^,],%[^,],%[^\n]\n",
                  full_appointment[full_appointment_count].service, full_appointment[full_appointment_count].date,
                  full_appointment[full_appointment_count].time, full_appointment[full_appointment_count].doctor,
                  full_appointment[full_appointment_count].name, full_appointment[full_appointment_count].phone) == 6)
    {
        full_appointment_count++; // Read each line from the file and store its values in the schedule_list array and increase the full_appointment_count for each successfully loaded admin appointment
    }
	// Close the file after reading
    fclose(adminFile);
}

void selectDate(char date[99]) 
{
    int choice_date;
    int i;
	// The number of days to generate
	int num_days = 7;
	char** available_dates = show_available_dates(num_days);
	

    fflush(stdin);
    printf("\nSelect a date:\n");
    // Print the formatted date strings
    for (i = 0; i < num_days; i++) 
	{
        printf("%d. %s\n", i+1, available_dates[i]);
    }	    
    printf("Enter your choice: ");
    
    // Input validation loop for date choice
	while (1) 
	{
        scanf("%d", &choice_date);
        if (choice_date >= 1 && choice_date <= 7) 
		{
            break; // Exit the loop if a valid choice is made
        } 
		else 
		{
            printf("\nInvalid selection. Re-enter your choice : ");
        }
    }
	choice_date--;
    strcpy(date, available_dates[choice_date]);
}

void selectTime(char time[99]) 
{
    int choice_time;

        fflush(stdin);
        printf("\nSelect a time:\n");
        printf("1. 08:00 AM\n");
        printf("2. 09:00 AM\n");
        printf("3. 10:00 AM\n");
        printf("4. 11:00 AM\n");
        printf("5. 02:00 PM\n");
        printf("6. 03:00 PM\n");
        printf("7. 04:00 PM\n");
        printf("8. 05:00 PM\n");
        printf("Enter your choice for time selection: ");
        
        // Input validation loop for time choice
    while (1) 
	{
        scanf("%d", &choice_time);
        if (choice_time >= 1 && choice_time <= 8) 
		{
            break; // Exit the loop if a valid choice is made
        } 
		else 
		{
            printf("\nInvalid selection. Re-enter your choice : ");
        }
    }

    switch (choice_time) 
	{
        case 1:
            strcpy(time, "08:00 AM");
            break;
        case 2:
            strcpy(time, "09:00 AM");
            break;
        case 3:
            strcpy(time, "10:00 AM");
            break;
        case 4:
            strcpy(time, "11:00 AM");
            break;
        case 5:
            strcpy(time, "02:00 PM");
            break;
        case 6:
            strcpy(time, "03:00 PM");
            break;
        case 7:
            strcpy(time, "04:00 PM");
            break;
        case 8:
            strcpy(time, "05:00 PM");
            break;
    }
}

void selectService(char service[99]) 
{
    int choice;

    printf("\n1. Outpatient Treatment");
    printf("\n2. Quit Smoking Service");
    printf("\n3. Pre-Marital Screening");
    printf("\n4. Medical check up");
    printf("\n5. Dental check up");
    printf("\n\nSelect a service : ");

    // Input validation loop for service choice
    while (1) 
	{
        scanf("%d", &choice);
        if (choice >= 1 && choice <= 5) 
		{
            break; // Exit the loop if a valid choice is made
        } 
		else 
		{
            printf("\nInvalid selection. Re-enter your choice : ");
        }
    }
	
	// Map the user's choice to the corresponding service
    switch (choice) 
	{
        case 1:
            strcpy(service, "Outpatient Treatment");
            break;
        case 2:
            strcpy(service, "Quit Smoking Service");
            break;
        case 3:
            strcpy(service, "Pre-Marital Screening");
            break;
        case 4:
            strcpy(service, "Medical check up");
            break;
        case 5:
            strcpy(service, "Dental check up");
            break;
    }
}

int selectDoctor(char doctor[99], const char doctors[MAX_DOCTORS][50], int appointment_count, const char date[99], const char time[99]) 
{
    char choice_doc;
    int choice_doc2, i, j;
    int doctorAvailable = 1;

    while (1) 
	{
        fflush(stdin);
        printf("\nDo you need a specific doctor? [Y|N]: ");
        scanf("%c", &choice_doc);

        if (choice_doc == 'Y' || choice_doc == 'y') 
		{
            printf("\n1. Doctor Wee\n");
            printf("2. Doctor Lye\n");
            printf("3. Doctor Tan\n");
            printf("Select the doctor you wish to book an appointment with: ");
            scanf("%d", &choice_doc2);

            switch (choice_doc2) 
			{
                case 1:
                    strcpy(doctor, "Doctor Wee");
                    break;
                case 2:
                    strcpy(doctor, "Doctor Lye");
                    break;
                case 3:
                    strcpy(doctor, "Doctor Tan");
                    break;
                default:
                    printf("\nInvalid selection. Please re-enter your choice.\n");
                    continue; // Restart the loop to re-enter the doctor choice
            }

            // Check if the selected doctor has any conflicting appointments
            doctorAvailable = 1;
            for (j = 0; j < full_appointment_count; j++) 
			{
                if (strcmp(date, full_appointment[j].date) == 0 &&
                    strcmp(doctor, full_appointment[j].doctor) == 0 &&
					strcmp(time, full_appointment[j].time) == 0) 
				{
                  	doctorAvailable = 0; // The doctor is not available at the chosen time
                 	break;
           		}
            }
			
			// Exit the loop whether the doctor is available or not available at the chosen time
            if (!doctorAvailable) 
			{
                break;
            }
            else
            {
            	break;
			}
		
        } 
		else if (choice_doc == 'N' || choice_doc == 'n') 
		{
            for (i = 0; i < MAX_DOCTORS; i++) 
			{
                int doctorAlreadyBooked = 0;

                for (j = 0; j < full_appointment_count; j++) 
				{
                    if (strcmp(date, full_appointment[j].date) == 0 &&
                        strcmp(time, full_appointment[j].time) == 0 &&
                        strcmp(doctors[i], full_appointment[j].doctor) == 0) 
						{
                        doctorAlreadyBooked = 1;
                        break;
                    	}
                }

                if (!doctorAlreadyBooked) 
				{
                    strcpy(doctor, doctors[i]);
                    doctorAvailable = 1;
                    break; // Exit the inner loop and assign the first available doctor
                }
            }
			
			// Exit the outer loop
            if (doctorAvailable) 
			{
                break;
            } 
			else 
			{
                break;
            }
        }
        else
        {
        	printf("\nInvalid selection.\n");
		}
    }
    return choice_doc;
}

char** show_available_dates(int num_days) 
{
	int SECONDS_PER_DAY = 86400;
    // Declare an array to store datetime values
    time_t datetime_values[num_days];

    // Get the current time
    time_t current_time;
    time(&current_time);

    // Skip the current day (today) by incrementing the current_time
    current_time += SECONDS_PER_DAY; // Add one day (in seconds)

    // Initialize a counter for the datetime array
    int i = 0;

    // Loop to generate datetime values for the next week (skipping weekends)
    while (i < num_days) 
	{
        // Calculate the timestamp for the next day
        current_time += SECONDS_PER_DAY; // Add one day (in seconds)

        // Get the day of the week for the next day
        struct tm *current_date = localtime(&current_time);
        int next_day = current_date->tm_wday;

        // Check if the next day is not a weekend (0 = Sunday, 6 = Saturday)
        if (next_day != 0 && next_day != 6) 
		{
            // Store the datetime value in the array
            datetime_values[i++] = current_time;
        }
    }

    // Define an array of weekday names
    char *weekday_names[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    // Define an array of months names
    char *month_names[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

    // Create an array of strings to store the formatted date strings
    char** formatted_dates = (char**)malloc(num_days * sizeof(char*));
	
	int j;
    // Format the date strings and store them in the array
    for (j = 0; j < num_days; j++) 
	{
        struct tm *date_info = localtime(&datetime_values[j]);
        char* formatted_date = (char*)malloc(50 * sizeof(char)); // Allocate space for the formatted date
        snprintf(formatted_date, 50, "%02d %s %04d (%s)", date_info->tm_mday, month_names[date_info->tm_mon], date_info->tm_year + 1900, weekday_names[date_info->tm_wday]);
        formatted_dates[j] = formatted_date;
    }

    return formatted_dates;
}

int username_validation(const char *username)
{
	char data_username[20], data_password[20];
	FILE *file1 = fopen("user_details.txt", "r");
    if (file1 == NULL) 
	{
        return 0; // File doesn't exist or unable to open
    }
    while(!feof(file1))
    {
    	fscanf(file1,"%s %s", data_username,data_password);
    	if (strcmp(username, data_username) == 0)
    	{
    		fclose(file1);
    		return 1;
		}
	}
	fclose(file1);
	return 0;
}

// Function to search for appointments by name
void searchAppointmentsByName() 
{
    int found = 0;
    char searchName[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Name");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the name to search for: ");
    gets(searchName);
    // Iterate through appointments
    for (count = 0; count < appointment_count; count++) 
    {
        if (strcmp(schedule_list[count].name, searchName) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", schedule_list[count].service);
            printf("Date: %s\n", schedule_list[count].date);
            printf("Time: %s\n", schedule_list[count].time);
            printf("Doctor: %s\n", schedule_list[count].doctor);
            printf("Name: %s\n", schedule_list[count].name);
            printf("Phone: %s\n", schedule_list[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given name.\n");
    }
}

// Function to search for appointments by contact
void searchAppointmentsByContact() 
{
    int found = 0;
    char searchContact[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Contact");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the contact to search for: ");
    gets(searchContact);
    // Iterate through appointments
    for (count = 0; count < appointment_count; count++) 
    {
        if (strcmp(schedule_list[count].phone, searchContact) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", schedule_list[count].service);
            printf("Date: %s\n", schedule_list[count].date);
            printf("Time: %s\n", schedule_list[count].time);
            printf("Doctor: %s\n", schedule_list[count].doctor);
            printf("Name: %s\n", schedule_list[count].name);
            printf("Phone: %s\n", schedule_list[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given contact.\n");
    }
}

void searchAppointmentsByService()
{
    int found = 0;
    char searchService[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Service");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the Service to search for: ");
    gets(searchService);
    // Iterate through appointments
    for (count = 0; count < appointment_count; count++) 
    {
        if (strcmp(schedule_list[count].date, searchService) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", schedule_list[count].service);
            printf("Date: %s\n", schedule_list[count].date);
            printf("Time: %s\n", schedule_list[count].time);
            printf("Doctor: %s\n", schedule_list[count].doctor);
            printf("Name: %s\n", schedule_list[count].name);
            printf("Phone: %s\n", schedule_list[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given Service.\n");
    }
}

void searchAppointmentsByDate()
{
    int found = 0;
    char searchDate[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Date");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the Date to search for: ");
    gets(searchDate);
    // Iterate through appointments
    for (count = 0; count < appointment_count; count++) 
    {
        if (strcmp(schedule_list[count].date, searchDate) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", schedule_list[count].service);
            printf("Date: %s\n", schedule_list[count].date);
            printf("Time: %s\n", schedule_list[count].time);
            printf("Doctor: %s\n", schedule_list[count].doctor);
            printf("Name: %s\n", schedule_list[count].name);
            printf("Phone: %s\n", schedule_list[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given date.\n");
    }
}

void searchAppointmentsByTime()
{
    int found = 0;
    char searchTime[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Time");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the Time to search for: ");
    gets(searchTime);
    // Iterate through appointments
    for (count = 0; count < appointment_count; count++) 
    {
        if (strcmp(schedule_list[count].date, searchTime) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", schedule_list[count].service);
            printf("Date: %s\n", schedule_list[count].date);
            printf("Time: %s\n", schedule_list[count].time);
            printf("Doctor: %s\n", schedule_list[count].doctor);
            printf("Name: %s\n", schedule_list[count].name);
            printf("Phone: %s\n", schedule_list[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given time.\n");
    }
}

void searchAllAppointmentsByName() 
{
    int found = 0;
    char searchName[50];
    
    printf("\n=========================================================");
    printf("\n\t\tSearch Appointments by Name");
    printf("\n=========================================================\n");

	fflush(stdin);
	printf("\nEnter the name to search for: ");
    gets(searchName);
    // Iterate through appointments
    for (count = 0; count < full_appointment_count; count++) 
    {
        if (strcmp(full_appointment[count].name, searchName) == 0) 
        {
            // Display matching appointment details
            printf("\nAppointment #%d\n", count + 1);
            printf("Service: %s\n", full_appointment[count].service);
            printf("Date: %s\n", full_appointment[count].date);
            printf("Time: %s\n", full_appointment[count].time);
            printf("Doctor: %s\n", full_appointment[count].doctor);
            printf("Name: %s\n", full_appointment[count].name);
            printf("Phone: %s\n", full_appointment[count].phone);
            
            found = 1;
        }
    }

    if (!found) 
    {
        printf("No appointments found for the given name.\n");
    }
}
