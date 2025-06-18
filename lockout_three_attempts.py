print("Enter username and password:")
count=3
for i in range(count):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password=="pass123" and username=="admin":
        print("Login successful!")
        break
    else:
        print("Login unsuccessful!")
        count -= 1
        print("Attempts left: ",count)
else:
    print("Account locked")
