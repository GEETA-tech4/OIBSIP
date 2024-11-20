weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))


BMI = weight / (height**2)
print(f"Your BMI is:{BMI:.2f}")

if (BMI<16):
    print ("You are severely underweight"),BMI

elif (BMI>=16 and BMI <18.5):
    print("You are Underweight"),BMI

elif (BMI>=18.5 and BMI <24):
     print("You are Healthy"),BMI

elif (BMI>=25 and BMI <30):
 print("You are Overweight"),BMI
 
elif(BMI >=30):
    print("You are Obese"),BMI
