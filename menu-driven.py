class Student:

    def __init__(self):
        self.rollno = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.marks = int(input("Enter marks: "))

    def update_mark(self):
        self.marks = int(input("Enter new marks: "))

    def display(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Marks:", self.marks)


l = []

while(1):

    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = Student()
        l.append(s)

    elif ch == 2:
        roll = int(input("Enter roll number: "))

        for i in l:
            if i.rollno == roll:
                i.update_mark()
                break
        else:
            print("Student not found")

    elif ch == 3:
        for i in l:
            i.display()

    elif ch == 4:
        roll = int(input("Enter roll number: "))

        for i in l:
            if i.rollno == roll:
                print("Student found")
                i.display()
                break
        else:
            print("Student not found")

    elif ch == 5:
        roll = int(input("Enter roll number: "))

        for i in l:
            if i.rollno == roll:
                l.remove(i)
                print("Student deleted")
                break
        else:
            print("Student not found")

    elif ch == 6:
        break

    else:
        print("Invalid choice")