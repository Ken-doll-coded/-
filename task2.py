class pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, "-", pupil.mar)
