height = float(input("What is your height?"))
weight = float(input("What is your weight?"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = round(weight/(height * height), 2)

print("Here is your BMI: " + str(bmi))
