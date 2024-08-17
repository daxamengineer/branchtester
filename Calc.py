import add
import Subtraction
import multiplication
import Division

print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")


while(1):
    choice = int(input("Enter Choice of Operation: "))

    num1 = int(input("Enter Num 1 - "))
    num2 = int(input("Enter Num 2 - "))

    if choice == 1:
        res = add.add(num1, num2)
    elif choice == 2:
        res = Subtraction.Subtract(num1, num2)
    elif choice == 3:
        res = multiplication.multiply(num1, num2)
    elif choice == 4:
        res = Division.division(num1, num2)
    elif choice == 5:
        break

    print("Result - ", res)