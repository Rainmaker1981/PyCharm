from User import User

class Student(User):
    __student_id = None

    def __init__(self, first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.set_student_id(student_id)

# helpers

# getters
    def get_student_id(self):
        return self.__student_id

# setters
    def set_student_id(self, student_id):
        self.__student_id = student_id

# string
    def __str__(self):
        return "Student:" + super().__str__()[5:] + "\tID #: " + str(self.get_student_id()) + "\n"
