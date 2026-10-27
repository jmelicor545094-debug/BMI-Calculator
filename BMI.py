
while True:
    print("================================")
    print("         BMI CALCULATOR")
    print("================================")
    print("1. Calculate BMI")
    print("2. View BMI Categories")
    print("3. Exit")
    print("================================")
    choice = input("Enter your choice: ").strip()
    print()

    if choice == "1":
        name = input("Enter your name: ").strip()

        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
        except ValueError:
            print("Invalid input. Weight and height must be greater than zero.")
            print()
            continue

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be greater than zero.")
            print()
            continue

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print("================================")
        print("           BMI RESULT")
        print("================================")
        print(f"Name: {name}")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("================================")
        print()

    elif choice == "2":
        print("BMI CATEGORIES")
        print("Below 18.5       : Underweight")
        print("18.5 to below 25 : Normal weight")
        print("25 to below 30   : Overweight")
        print("30 and above    : Obesity")
        print()

    elif choice == "3":
        print("Thank you for using the BMI Calculator!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        print()
