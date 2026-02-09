from Circle import Circle
from Rhombus import Rhombus
from Airplane import Airplane

def main():
    c1 = Circle(5)
    c2 = Circle(7)
    print(c1)
    print(c2)
    print("c1 radius:", c1.get_radius())
    print("c1 area:", c1.get_area())
    print("Compare: ", c1.compare_to(c2))
    print("Equal: ", c1.equal_to(c2))
    print()

    r1 = Rhombus(4, 6, 8)
    r2 = Rhombus(4, 5, 9)
    print(r1)
    print(r2)
    print("r1 side_length:", r1.get_side_length())
    print("r1 daig_1:", r1.get_daig_1())
    print("r1 diag_2:", r1.get_diag_2())
    print("r1 perimeter:", r1.get_perimeter())
    print("r1 area:", r1.get_area())
    print("Compare by area:", r1.compare_to(r2))
    print("Equal:", r1.equal_to(r2))
    print()

    a1 = Airplane("Boeing", "737 MAX", 2, 188, 521)
    a2 = Airplane("Airbus", "A320neo", 2, 180, 513)
    print(a1)
    print(a2)
    distance = 500
    print(f"Time to arrive for {distance} miles at top speed: ", round(a1.time_to_arrive(distance), 2))
    print("compare by top_speed:", a1.compare_to(a2))
    print("Is a1 equal to a2?:", a1.equal_to(a2))


if __name__ == "__main__":
    main()
