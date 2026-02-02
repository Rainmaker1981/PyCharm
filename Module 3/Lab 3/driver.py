from My_Circle import My_Circle as mc


def main():
    print("Mark Meyer \nCYBR 150 - Lab 3\nFeb 1, 2026\n\n")

    # task 4/5
    c1 = mc("c1", 2)
    c2 = mc("c2", 3)

    # task 6
    print(c1.get_name(), c1.get_radius())
    print(c2.get_name(), c2.get_radius())
    print()

    c1.set_radius(10)
    c1.set_name("circle_1")
    c2.set_radius(20)
    c2.set_name("circle_2")

    print("c1 name:", c1.get_name(), "radius:", c1.get_radius())
    print("c2 name:", c2.get_name(), "radius:", c2.get_radius())
    print()

if __name__ == "__main__":
    main()
