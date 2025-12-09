#notes on while loops

# name= input("enter your name")
# Given:




# while name == "":
#     print("you did not enter your name")
#     name = input("enter your name")
# print(f"hello {name}.")


# age = int(input("enter your age: "))

# while age < 0:
#     print("age cannot be negative")
#     age = int(input("enter your age: "))
# print(f"you are {age} years old")

# food = input("enter any food you like (q to quit): ")
# food_list=[]
# while not food == "q":
#     print("you like {food}")
#     food = input("enter any food you like (q to quit): ")
#     food_list.append(food)
#     print(food_list)
# print("bye")

# num= int(input("enter a number between 1-10"))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("enter a number between 1-10:"))
# print(f"your number is {num}")


# # Challenge:
colors = ["red", "blue", "green", "yellow", "purple"]
while index <len(colors):
    color= colors.pop(0)
    if color == "yellow":
        print(colors[index])
        index+= 1
# Do NOT print "yellow" — stop before it.
