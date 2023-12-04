import Student
import random

# Create a dictionary to store table info, key => table number, value => list of students at table
tables = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : []}

# Create roster of student objects
roster = []

chris = Student.Student('chris')
chris.cant_sit_with.append('darwin')
roster.append(chris)

darwin = Student.Student('darwin')
darwin.cant_sit_with.append('chris')
roster.append(darwin)

kellen = Student.Student('kellen')
roster.append(kellen)

eddy = Student.Student('eddy')
roster.append(eddy)

aiden = Student.Student('aiden')
roster.append(aiden)

amy = Student.Student('amy')
roster.append(amy)

joshua_h = Student.Student('joshua h')
joshua_h.cant_sit_with.append('chris')
joshua_h.cant_sit_with.append('darwin')
roster.append(joshua_h)

landon = Student.Student('landon')
roster.append(landon)

olive = Student.Student('olive')
roster.append(olive)

maxamilian = Student.Student('maxamilian')
roster.append(maxamilian)

king = Student.Student('king')
roster.append(king)

cameron = Student.Student('cameron')
cameron.cant_sit_with.append('ferris')
roster.append(cameron)

ferris = Student.Student('ferris')
ferris.cant_sit_with.append('cameron')
roster.append(ferris)



# Create duplicate of roster named students that we can modify during the process
students = roster.copy()

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
