# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
x = 365 * 90 - age * 365
y = 52 * 90 - age * 52
z = 12 * 90 - age * 12
print(f"You have {x} days, {y} weeks, and {z} months left.")
