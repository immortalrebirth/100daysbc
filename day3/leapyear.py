# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#if year % 4 == 0 and year % 100 != 0:
#    print("Leap year.")
#elif year % 100 == 0 and year % 400:
#    print("Leap year.")
#else:
#    print("Not leap year.")
#nested if else below, above is using or and and
if year % 4 == 0:
   if year % 100 != 0:
       print("Leap year.")
   else: 
       if year % 400:
           print("Leap year.")
else:
    print("Not leap year.")
