# It's simple calculator program here in python and don't udge me based on this.....................
import math

print("Processding with your code...")
print("Welcome to the simple calculator!")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Expoential\n6.Squatroot\n7.Sine\n8.Cosine\n9.Tan\n10.Cot\n11.Secant\n12.Cosecant")
n = int(input("Enter the operation number you want to perform: "))
if n==1:
         a = int(input("Enter the first number:" ))
         b = int(input("Enter the second number:" ))
         print(f"The sum is{a+b}")
elif n==2:
        a = int(input("Enter the first number:" ))
        b = int(input("Enter the second number:" ))
        print(f"The subtraction result is {a-b}")
elif n==3:
        a = int(input("Enter the first number:" ))
        b = int(input("Enter the second number:" ))
        print(f"When {a} multiplied with {b}, the result would be {a*b}")
elif n==4:
        a = int(input("Enter the first number:" ))
        b = int(input("Enter the second number:" ))
        print(f"The division result is {a/b}")
elif n==5:
        a = int(input("Enter the first number:" ))
        b = int(input("Enter the second number:" ))
        print(f"When {a} is raised to {b},the result is {a**b}")
elif n==6:
        c = int(input("Enter a number:"))
        print(f"The square root of {c} is {math.sqrt(c)}")
elif n ==7:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Sine value is {math.sin(c)}")
elif n ==8:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Cosine value is {math.cos(c)}")
elif n ==9:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Tan value is {math.tan(c)}")
elif n == 10:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Cot value is: {1/math.tan(c)}")
elif n == 11:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Secant valie is {1/math.cos(c)}")
elif n ==12:
        c = int(input("Enter a number:"))
        c = math.radians(c)
        print(f"Coseant value is {1/math.sin(c)}")
else:
        print("Invalid operation number. Exiciting...")
