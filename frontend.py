# Hospital_System
from patient_mgr import PatientMgr


class FrontEnd:
    def __init__(self):
        self.PM = PatientMgr()
    
    def print_dachbord():
        msgs = ["Programe options:","1) Add a new patient","2) List all patients",
        "3) Go to next patient","4) remove a leaving patient","5) End the program"]
        print('\n'.join(item for item in msgs)
        )

    def choice_valid(self,choice):
        return ( choice  and 48 < ord(choice[0]) <= 53  and 1 <= int(choice) <= 5 )

    def specialization_valid(self,special):
        return ( special  and 48 < ord(special[0]) <= 68 and 1 <= int(special) <= 20 )      

    def show_menu(self,choice):    
        choice = int(choice)
        if choice == 1:
            specialization = input("Enter specialization (from 1 to 20): ")
            if self.specialization_valid(specialization):
                specialization = int(specialization)
            else:
                print("enter a valid specialization from 1 to 20")
                return ""    
            name = input("Enter patient name: ")
            status = int(input("Enter status (0 Normal / 1 Urgent / 2 Super urgent): "))
            self.PM.add_new_patient(specialization,name,status)
        elif choice == 2:
            self.PM.list_all_patients()    
        elif choice == 3:
            specialization = int(input("Enter specialization (from 1 to 20): "))
            self.PM.get_next_patient(specialization)
        elif choice == 4:
            specialization = int(input("Enter specialization (from 1 to 20): "))
            name = input("Enter patient name: ")  
            self.PM.remove_leaving_patient(specialization,name)
        elif choice == 5:
            self.PM.end_program()