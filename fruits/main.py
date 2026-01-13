print("hello")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
user_input = input("Enter your favorite fruit: ")
if user_input in fruits:
    print("You chose a popular fruit!")
else:
    print("Sorry, that's not on the list. There are only: " + ", ".join(fruits))
    
print("test1")