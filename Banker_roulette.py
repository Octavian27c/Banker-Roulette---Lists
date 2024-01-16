import random

names = ["Angela", "Ben", "Jenny", "Michael", "Cloe"]
 
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

# Get the total nubers of items on the list.
no_friends = len(names)

# Generate random numbers betwen 0 and the last index.
random_friend = random.randint(0, no_friends-1)

#Pick out random person from he list of naes using the random number.
person_who_will_pay = names[random_friend]

#Print the name
print(person_who_will_pay + " is going to buy the meal today!")