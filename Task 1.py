def factorial():
    num = int(input("Enter the number: "))
    b = 1
    for i in range(num , 0 , -1):
        b = b*i
    print(f"Factorial of {num} is {b}")
factorial()

