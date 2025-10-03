try:
    n = int(input("Enter a Number: "))
except ValueError:
    print("Please enter a number!")
else:
    for i in range(1, n + 1):
        square = i * i
        print(square)