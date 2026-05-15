print("this is a BMI calculator")
name=input("Enetr your name:")
Weight=float(input("Enter your weghit"))
height=float(input("Enter your height"))
bmi= Weight /(height/100)**2
if bmi<18.5:
    print(f"{name},you are under Weight.your BMI is{bmi}")
if bmi >=18.5 and bmi <24.999:    
    print(f"{name},you are noraml and healthy Weight.your BMI is{bmi}")
if bmi >=25 and bmi <29.9:    
    print(f"{name},you are over Weight.your BMI is{bmi}")
if bmi >=30 and bmi <34.9:    
    print(f"{name},you are obase Weight.your BMI is{bmi}")
if bmi>=35:
    print(f"{name},you are extremly Weight.your BMI is{bmi}")

