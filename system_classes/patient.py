# Hospital_System


class Patient:
    def __init__(self,name,status):
        self.name,self.status = name,status

    def __str__(self):
        return f"the patient name is: {self.name}, patient status is: {self.status}"

    def __repr__(self):
        return f"the patient name is: {self.name}, patient status is: {self.status}"              