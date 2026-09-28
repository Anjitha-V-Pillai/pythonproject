class Hospital:
    def __init__(self):
        self.hos_name=input("Enter the hospital name:")
        self.location=input("Enter the location:")
        self.phone=int(input("Enter the phone number:"))

    def display_hospital(self):
        print("hospital name:",self.hos_name)
        print("location:",self.location)
        print("phone:",self.phone)

class Department:
    def __init__(self):
            self.dept_name=input("Enter the department name:")
            self.doctor_name=input("Enter the doctor name:")
    def display_department(self):
            print("department name:",self.dept_name)
            print("doctor name:",self.doctor_name)

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("Enter the patient name:")
        self.age=int(input("Enter the age of the patient:"))
        self.gender=input("Enter the gender of the patient:")
        self.phone=int(input("Enter the phone number:"))
        self.bed_no=int(input("Enter the bed number:"))
        self.discharge_date=input("Enter the discharge date:")

    def set_discharge(self):
        self.discharge_date=input("Enter the update discharge date:")
    def full_summary(self):
        # print("hospital name:",self.hos_name)
        # print("location:",self.location)
        # print("phone:",self.phone)
        # print("department name:",self.dept_name)
        # print("doctor name:",self.doctor_name)
        print("patient aummary")
        Hospital.display_hospital(self)
        Department.display_department(self)
        print("patient name:",self.patient_name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("bed number:",self.bed_no)
        if (self.discharge_date==""):
            print("Not yet discharged")
        else:
            print("discharge date:",self.discharge_date)

p=Patient()
p.full_summary()

p.set_discharge()
p.full_summary()
