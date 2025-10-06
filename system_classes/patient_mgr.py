# Hospital_System
from system_classes.patient import Patient

Specials = 20
Max_patients = 10

class PatientMgr:
    def __init__(self):
        self.specializations = [[None for _ in range(Max_patients)] for _ in range(Specials)]
        
    def check_availability(self,specialization):
        idx = specialization -1
        if 1 <= specialization <= Specials:
            if any(slot is None for slot in self.specializations[idx] ):
                return True
        return False

    def get_status(self,patient):
        if patient is not None:
            return patient.status
        return ""

    def patient_priority_check(self,specialization):
        idx = specialization-1
        patients = [p for p in self.specializations[idx] if p is not None]
        sorted_patients = sorted(patients,key = self.get_status,reverse=True)
        return sorted_patients + [None]*(Max_patients-len(sorted_patients))

    def add_new_patient(self,specialization,name,status):
        if self.check_availability(specialization):
            idx = specialization-1
            patient = Patient(name,status)
            for i in range(Max_patients):
                if self.specializations[idx][i] is None:
                    self.specializations[idx][i] = patient
                    break
            self.specializations[idx]= self.patient_priority_check(specialization)
        else:
            print("The specialization is full of patients now...please wait")
    
    def list_all_patients(self):
        for idx in range(Specials):
            print(f"Specialization {idx+1}:")
            for i in range(Max_patients):
                if self.specializations[idx][i] is not None:
                    patient = self.specializations[idx][i]              
                    print(f"     -Patient name: {patient.name}",end="")
                    if patient.status == 0:
                        print(f" , status: Normal") 
                    elif patient.status == 1:
                        print(f" , status: Urgent")
                    elif patient.status == 2:
                        print(f" , status: Super urgent")          
                else:
                    print("     -[Empty slot]") 
    
    def get_next_patient(self,specialization):
        idx = specialization-1
        if all(patient is None for patient in self.specializations[idx] ):
            print("No patients remain")
            return ""
        else:
            next_patient = self.specializations[idx].pop(0)
            self.specializations[idx].append(None)
            print(f"The next patient is {next_patient.name}, go to specialization {specialization}")   
    
    def remove_leaving_patient(self,specialization,name):
        found = False
        for idx,patient in enumerate(self.specializations[specialization-1]):
            if patient is not None and name == patient.name:
                next_patient = self.specializations[specialization-1].pop(idx)
                found = True
                break
        if found:
            self.specializations[specialization-1].append(None)
        else:
            print("this patient isn't exist")
    def end_program(self):
        print("\n\nThank you for using our hospital system...Goodbye!\n\n")
        exit(1)





