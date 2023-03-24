
first_number = float(input("first number:"))
second_number = float(input("second number:"))
math_heandling = input("enter sign\n"
                       "+\n"
                       "-\n"
                       "*\n"
                       "/\n"
                       "your choice:")
match math_heandling:
    case "+":
        print(first_number + second_number)
    case "-":
        print(first_number - second_number)
    case "*":
        print(first_number * second_number)
    case "/":
        if second_number == 0:
            print("Your math teacher looks at you with disapproval,YOU ENTERED 0\n"
                  "Can't divide by 0")
        else:
            print(first_number / second_number)
