import pandas as pd
import Student
import random

# Create a dictionary to store table info, key => table number, value => list of students at table
tables = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : []}

# Read roster spreadsheet into dataframe

rosterFrame = pd.read_excel('period1.xlsx')
rosterFrame.fillna('none')

# convert dataframe data into student objects in list 'roster'

roster = []

for ind in rosterFrame.index:

    roster.append(Student.Student(rosterFrame['First Name'][ind]))

    if str(rosterFrame['No'][ind]) != 'none':

        roster[ind].cant_sit_with = (str(rosterFrame['No'][ind])).split(', ')



# Create duplicate of roster named students that we can modify during the process
students = roster.copy()

# Method for generating random seating chart

cont = True

while cont:
    
    students = roster.copy()
    table_num = 1
    
    # Clear tables
    for i in range(1, 8):
        tables[i] = []
        
    cont = False
    
    while students:

        student_num = random.randint(0, len(students) - 1)

        if len(tables[table_num]) >= 4:

            table_num += 1

        # Add random student to table
        tables[table_num].append(students[student_num])

        # Check if student can sit here
        for x in students[student_num].cant_sit_with:
            
            for y in tables[table_num]:
                
                if x == y.name:

                    students = []
                    cont = True
                    break

        # If students wasnt wiped, remove student we added to a table
        if students:
            
            students.pop(student_num)


for k, v in tables.items():
    print(k)
    for s in v:
        print(s.name)
    print("")
