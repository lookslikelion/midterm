from this import d


name = input("What is your name?")
height = float(input("What is your height(cm)?"))
weight = float(input("What is your weight(kg)?"))
bmi = (weight / ((0.01)*height)**2)
print("BMI of", name, "is", round(bmi,4))