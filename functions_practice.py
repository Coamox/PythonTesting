
print("Hello from inside a file!")

def hello():
    print("Welcome to my file new user!")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(lunchlist):
    if len(lunchlist) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunchlist)):
            if i == 0:
                print(f"First I eat {lunchlist[0]}")
            else:
                print(f"Next I eat {lunchlist[i]}")

    
hello()
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["Pizza"])
eat_lunch(["Pasta", "Chicken", "Cake"])