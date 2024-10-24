import pandas as pd
from typing import List, Dict
import random

class Student:

    # Student class for creating student objects with attributes:
    # name (string, the students name)
    # cant_sit_with (list, other student names as strings that this student cant sit with)
    # wants_to_sit_with (list, other student names as strings that this student wants to sit with/wokrs well with)

    # Constructor
    def __init__(self, name: str):
        self.name = name
        self.cant_sit_with: List[str] = []
        self.wants_to_sit_with: List[str] = []

def read_roster(file_path: str) -> List[Student]:
    
    # Function that takes the roster excel file and returns a list of student objects

    roster_frame = pd.read_excel(file_path)
    roster_frame = roster_frame.fillna('none')
    roster = []

    for _, row in roster_frame.iterrows():
        student = Student(row['First Name'])
        if str(row['No']) != 'none':
            student.cant_sit_with = str(row['No']).split(', ')
        if 'Yes' in row and str(row['Yes']) != 'none':
            student.wants_to_sit_with = str(row['Yes']).split(', ')
        roster.append(student)

    return roster

def get_score(tables: Dict[int, List[Student]]) -> int:

    # Function that looks at a seating chart and returns its score
    # Scoring weights can be modified by changing the numbers that are added or subtracted

    score = 0
    for table in tables.values():
        for student in table:
            for other_student in table:
                if other_student.name in student.cant_sit_with:
                    score -= 1
                if other_student.name in student.wants_to_sit_with:
                    score += 0.5
    return score

def generate_seating_chart(roster: List[Student]) -> Dict[int, List[Student]]:

    # Function that generates a random seating chart

    students = roster.copy()

    num_students = len(students)
    
    # Calculate number of tables with 4 students and 3 students
    num_tables_of_4 = num_students % 4  # The number of tables that should have 4 students
    num_tables_of_3 = (num_students - (num_tables_of_4 * 4)) // 3  # Remaining tables with 3 students
    total_tables = num_tables_of_4 + num_tables_of_3
    
    tables = {i: [] for i in range(1, num_tables_of_3 + num_tables_of_4 + 1)} # Create empty tables
    table_num = 1  

    while students:
        student = students.pop(random.randint(0, len(students) - 1))

        # Ensure the table is valid for this student
        table = tables[table_num]
        wants_to_sit_count = sum(1 for s in table if s.name in student.wants_to_sit_with)

        # Determine if the current table should have 3 or 4 students
        max_size = 4 if table_num <= num_tables_of_4 else 3  # First tables get 4, others get 3

        if len(table) < 4 and wants_to_sit_count < 2:  # Check table size and seating preference
            table.append(student)
        else:
            table_num = (table_num % total_tables) + 1  # Move to the next table
            tables[table_num].append(student)

        # Move to next table if current one is full
        if len(tables[table_num]) >= max_size:
            table_num = (table_num % total_tables) + 1

    return tables


def find_best_seating_chart(roster: List[Student], iterations: int = 10000) -> List[Dict[int, List[Student]]]:
    
    # Function that generates 10000 random seating charts and returns the 3 with the best scores

    best_tables = []
    
    for _ in range(iterations):
        tables = generate_seating_chart(roster)
        score = get_score(tables)
        best_tables.append((score, tables))
    
    best_tables.sort(key=lambda x: x[0], reverse=True)
    
    return best_tables[:3]

def print_arrangement(tables: Dict[int, List[Student]], score: int):

    # Function to print our output
    
    print(f"Seating Chart Score: {score}")
    print("")
    for table_num, students in tables.items():
        print(f"Table {table_num}:")
        for student in students:
            print(f"  {student.name}")
        print()

def main():
    
    roster = read_roster('period7.xlsx')
    best_tables = find_best_seating_chart(roster)

    print("Top 3 Best Seating Charts:")
    for i, (score, tables) in enumerate(best_tables, 1):
        print(f"\n{i}. Best Seating Chart:")
        print_arrangement(tables, score)

if __name__ == "__main__":
    main()


