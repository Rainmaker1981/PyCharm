# import statements
from Exercise1 import Triangle
from Exercise2 import Rectangle
from Exercise3 import Student
from Exercise4 import Employee
from Exercise5 import Animal
from Exercise6 import House

def main():
    print("Mark Meyer \n Cyber 150 \n Class Exercise 1 \n Feb 1, 2026 \n\n")

    t1 = Triangle(10, 20)
    print(t1)

    r1 = Rectangle(10, 20)
    print(r1)

    s1 = Student("Mark", "Allen", "Meyer", "May 28, 1981")
    print(s1)

    e1 = Employee("E1234", "Mark", "Meyer", "89632408@nebraska.edu")
    print(e1)

    a1 = Animal("cheetah", 4, "medium", "Speedy")
    print(a1)

    h1 = House(3, 2, 2500, 450000)
    print(h1)

if __name__ == '__main__':
    main()
