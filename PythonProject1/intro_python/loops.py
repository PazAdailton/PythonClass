cars = ["ok", "ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the producion line!")
        break
    print(f"This cars is {status}")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")
