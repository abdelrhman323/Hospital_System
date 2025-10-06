# Hospital_System

from system_classes.frontend import FrontEnd as FE
manual_testing = False  # True: for manual injecting patients / False: auto-generating patients
frontend = FE(manual_testing) 

if __name__ == "__main__":    
    while True:
        frontend.print_dachbord()
        choice = input("Enter your choice (from 1 to 5): ")
        if not frontend.choice_valid(choice):
            print("Invalid range. Try again!")
            continue
        else:        
            frontend.show_menu(choice)