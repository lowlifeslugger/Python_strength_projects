import numpy as np
import matplotlib.pyplot as plt
# but lowlife slugger what if-
# nothing ever happens
# if you dont have matplot lib pre-installed on pc, just open command prompt and copy paste
# pip install matplotlib numpy

while True:
    try:
        a = int(input("Enter starting x value: "))
        b = int(input("Enter ending x value: "))
        c = int(input("Enter precision (e.g. 400): "))

        if c <= 0:
            print("Precision must be a positive number.")
            continue

        # make x range
        x = np.linspace(a, b, c)

        while True:
            expr = input("Enter equation in terms of x only (e.g. x**2, np.sin(x)): ")
            try:
                # evaluation of y wrt to x
                y = eval(expr, {"np": np, "x": x})

                plt.plot(x, y)
                plt.xlabel("x")
                plt.ylabel("y")
                plt.title("Math Graph")
                plt.grid()
                plt.show()
                break

            except (SyntaxError, NameError, TypeError):
                print("Invalid equation. Try again.")

    except ValueError:
        print("Please enter valid integers.")
