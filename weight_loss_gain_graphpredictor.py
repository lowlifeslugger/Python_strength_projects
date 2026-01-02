import numpy as np
import matplotlib.pyplot as plt

# the lowlifeslugger does not concern himself with the emotional hollowness he feels
 
while True:
    try:
        height = int(input("Enter height in cm: "))
        weight = float(input("Enter weight in kg: "))
        age = int(input("Age in years: "))
        AF = float(input(
            "---Activity Factor---\n"
            "sedentary (little exercise) - 1.2\n"
            "lightly active (1-3 days exercise) - 1.375\n"
            "moderate (3-5 days) - 1.55\n"
            "very active (6-7 days) - 1.725\n"
            "extra active (hard work) - 1.9\n"
            "Enter number: "
        ))
        Cals = float(input("Enter calories consumed per day: "))
        days = int(input("Enter number of days to plot: "))
        sex = input("Enter gender (m/f): ").lower().strip()

        if sex not in ["m", "f"]:
            print("Invalid gender input. Try again.")
            continue

        weights = [weight]

        for day in range(days):
            W = weights[-1]

            # Mifflin-St Jeor equation
            if sex == "m":
                BMR = 10*W + 6.25*height - 5*age + 5
            else:
                BMR = 10*W + 6.25*height - 5*age - 161

            TDEE = AF * BMR
            delta_W = (Cals - TDEE) / 7700
            W_next = W + delta_W
            weights.append(W_next)

        # Plot once after the loop
        plt.figure(figsize=(10,5))
        plt.plot(range(days+1), weights, marker='o')
        plt.xlabel("Days")
        plt.ylabel("Weight (kg)")
        plt.title("Weight Change Over Time")
        plt.grid(True)
        plt.show()
        break  # exit the while loop after successful run

    except ValueError:
        print("I was sent here to destroy you ")
