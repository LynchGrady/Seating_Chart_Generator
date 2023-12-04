class Student:

    # Student class for creating student objects with attributes:
    # name (string, the students name)
    # cant_sit_with (list, other student names as strings that this student cant sit with)

    # Constructor
    def __init__(self, name):
        self.name = name
        self.cant_sit_with = []
