# Activity 1 
print("==========")
print("Welcome here")
print("My first post!")
print("==========")

# 'q' to escape the terminal after running

# Activity 2
username = "cool_creator"
bio = "Fun Blogger"
follwers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", follwers)

# Activity 3
follwers += 50
print("Day 1:", follwers)

follwers += 20
print("Day 2:", follwers)

follwers -= 10
print("Day 3:", follwers)

# Activity 4
# username = input("Enter Username: ")
# age = input("Enter Age: ")
# category = input("Enter Content Category: ")

# print("\n Instagram Profile")
# print("==========")
# print("Username:", username)
# print("Age:", age)
# print("Content Category:", category)

# Activity 5
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\n Instagram Profile")
print("==========")
print("Username:", username)
print("Age:", age)
print("Content Category:", category)
if age>40 and category == "fun":
    print("You are old, what is fun for you??")