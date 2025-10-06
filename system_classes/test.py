# testing of Hospital_System
from system_classes.patient_mgr import PatientMgr
PM = PatientMgr()
# Constants
Same = 0
Varies = 1
STS = [0, 1, 2]  # Example statuses: 0 = Admitted, 1 = Discharged, 2 = Under Observation

class Dummydata:
    def __init__(self,patient_mgr):
        self.PM = patient_mgr


    def generate_patients(self,specialization, number_of_patients, status_varity, status):
        generated = []
        for idx in range(number_of_patients):
            name = f"Dummy{idx}"
            status = status if status_varity == Same else STS[idx % len(STS)]
            self.PM.add_new_patient(specialization, name, status)
            generated.append((name, status))
        return generated
