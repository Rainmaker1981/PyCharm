from Student import Student
from Employee import Employee
from Admin import Admin

from Kitchen import Kitchen
from Bedroom import Bedroom
from Garage import Garage

from Dishwasher import Dishwasher
from Refrigerator import Refrigerator
from Freezer import Freezer


def main():
    # Exercise 1
    s1 = Student("Mark", "Meyer", 1234)
    e1 = Employee("Adam", "Spanier", "M.A.")
    a1 = Admin("Lori", "Skarka", "Secret")

    print(s1)
    print(e1)
    print(a1)

    # Exercise 2
    k1 = Kitchen(12, 14, "GE")
    b1 = Bedroom(11, 13, "Blue")
    g1 = Garage(24, 22, 2)

    print(k1)
    print(b1)
    print(g1)

    # Exercise 3
    d1 = Dishwasher("Dishwasher", "Bosch", "12 place settings")
    r1 = Refrigerator("Refrigerator", "Samsung", "25 cu ft")
    f1 = Freezer("Freezer", "Whirlpool", "-10 F")

    print(d1)
    print(r1)
    print(f1)


if __name__ == "__main__":
    main()