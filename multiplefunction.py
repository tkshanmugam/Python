class multipleFuntion():
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2) == 1):
            print("odd Number")
            message = "odd Number"
        else:
            print("Even number")
            message = "Even number"
        return message; 
    def BMI():
        # Input weight in kilograms and height in meters
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
        bmi = weight_kg / (height_m ** 2)
        if bmi < 18.5:
            print("You are underweight.")
            message = "You are underweight."
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
            message = "You have a normal weight."
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
            message = "You are overweight."
        else:
            print("You are obese.")
            message = "You are obese."