
#3.Given a dictionary
#
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
               'Amal':{'maths':40,'science':45,'english':48,'history':43},
              'Anu':{'maths':45,'science':46,'english':47,'history':49}}

#print the mark of Amal in the subject History
print(student_marks['Amal']['history'])

#Update the mark of Arun in maths to 35
student_marks['Arun']['maths']=35
print(student_marks['Arun'])

#print the marks of all students (in all subject
print(student_marks)
