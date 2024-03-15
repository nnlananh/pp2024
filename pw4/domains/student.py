class Student:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)
