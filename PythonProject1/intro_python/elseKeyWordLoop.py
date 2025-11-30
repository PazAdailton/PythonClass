cars = ["ok", "ok", "ok", "ok", "faulty"]
all_successful = True
for status in cars:
    if status == "faulty":
        print("Stpping the producion line!")
        all_successful = False
        break
    print(f"This car is {status}")
    print("Shipping a new car to customer!")

else:
    print("All cars built successfully. No faulty cars!")



for n in range(2,100):
    for x in range (2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")





#for f in range(2,20,3):
    #print(f)