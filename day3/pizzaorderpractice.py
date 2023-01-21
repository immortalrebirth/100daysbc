# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = size.lower()
add_pepperoni = add_pepperoni.lower()
extra_cheese = extra_cheese.lower()
if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3
else:
    bill = 0
    print("You didnt order anything.") 
if extra_cheese == "y":
    bill += 1
print(f"Your final bill is: ${bill}.")
