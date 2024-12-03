def square(num1, num2):
    squares = [x ** 2 for x in range(num1, num2 + 1)]

    odd_squares = [x for x in squares if x % 2 != 0]
    even_squares = [x for x in squares if x % 2 == 0]

    print("Square number :", squares)
    print("Odd square number :", odd_squares)
    print("Even square number :", even_squares)

num3 = int(input("Enter the 1st number : "))
num4 = int(input("Enter the 2nd number : "))
square(num3, num4)