import math
number_a = float(input("Input a:"))
number_b = float(input("Input b:"))
number_c = float(input("Input c:"))


discriminant_formula = math.pow(number_b,2)-4*(number_a*number_c)
if discriminant_formula > 0:
    first_formula_x1 = (-number_b + math.sqrt(discriminant_formula))/(2*number_a)
    second_formula_x2 = (-number_b - math.sqrt(discriminant_formula))/(2*number_a)
    print("x1=",first_formula_x1)
    print("x2=",second_formula_x2)
elif discriminant_formula == 0:
    formula_for_x = (number_b/(2*number_a))*-1
    print("x=",formula_for_x)
else:
    print("For the discriminant is 0, there are no roots")
