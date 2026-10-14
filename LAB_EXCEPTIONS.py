def additoin(x, y):

    x = 10
    y = 20
    try:
        print("Addition:", x + b)
    except NameError:
        print("Check the names in the printout.")
    except Exception as f:
        print(f.__class__)
        print("Try again Something's wrong.")
    else:
        print("The program is successful.")


additoin(10, 20)