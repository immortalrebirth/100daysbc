# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
randomrange = len(names)
randomrange -= 1
#cannot use random as a variable, int, it would mess up something as it is the same name as the imported module
randomperson = random.randint(0,randomrange)
print(f"{names[randomperson]} is going to buy the meal today!")
#below uses random.choice() to randomize name from list instead of using random integer
personpaying = random.choice(names)
print(personpaying)
