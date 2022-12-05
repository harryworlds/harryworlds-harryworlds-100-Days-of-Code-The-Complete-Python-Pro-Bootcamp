name = input("Hello, what is your name?   ")
print("")
greeting = print("Nice to meet you,", name, "and you can call me harry ")
print("")
print("Today, we are checking your body mass index")
print("")
#Variable height and weight
height_in_cm = input("Enter your height in cm: ")
print("")
weight = input("Enter your weight in kg: ")

#Conversion of unit
height_in_meter = float(height_in_cm) * 0.01

#Calculator
bmi = float(weight) / (float(height_in_meter)**2)
#Two decimal place
bmi_v2 = round(bmi, 2)

print("")
print("Your body mass index is", bmi_v2)

print("")
#Result & comment
if bmi_v2 <= 18:
    print("You body is underweight")
elif bmi_v2 <= 24.99:
    print("Your body is healthy")
elif bmi_v2 <= 29.99:
    print("Your body is over weight")
elif bmi_v2 <= 40:
    print("Your body is obese")
elif bmi_v2 <= 42:
    print("You body is extremely obese")
else:
    print("Your body BMI is", bmi_v2, " and it is above 42, which is extremely serious")

print("")
print("link for BMI char")
print("https://medical.azureedge.net/images/0aa8713b-421f-445f-996a-0aed1695b5a2.jpg")

print("")
print("link for NHS calulator")
print("https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/")