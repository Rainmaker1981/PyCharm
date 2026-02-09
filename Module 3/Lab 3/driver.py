from My_Circle import My_Circle as mc


def main():
    c1 = mc("circle_1", 20)
    c2 = mc("circle_2", 30)
    c3 = mc("circle_1", 20)

    # String function testing
    print(c1)
    print(c2)
    print(c3)

    # Test Equal
    print(c1.equal_to(c3))

    # Test Compare To
    print(c1.compare_to(c2))
    print(c2.compare_to(c1))
    print(c1.compare_to(c3))

if __name__ == "__main__":
    main()
