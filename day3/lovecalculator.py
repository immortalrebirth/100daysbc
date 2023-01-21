# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
combine_name = name1_lower + name2_lower
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
truecount = t + r + u + e
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
lovecount = l + o + v + e
truelove = int(f"{truecount}{lovecount}")
if truelove < 10 or truelove > 90:
    print(f"Your score is {truelove}, you go together like coke and mentos")
elif 40 < truelove < 50:
    print(f"Your score is {truelove}, you are alright together.")
else:
    print(f"Your score is {truelove}.")

