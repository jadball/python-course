def main():
    """ try different values of x and y to trigger exceptions"""
    try:
        x = 10
        y = 0

        if x > 150:
            raise Exception("x is much too big")
        if x > 50:
            raise Exception("x is too big")
        print(f"x is {x}")
        print(f"x/y is {x / y}")
    except Exception as e:
        print(e)


main()
