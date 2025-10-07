# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    x = num1
    y = num2
    z = num3
    return max(x, y, z)





# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    x = num1
    y = num2
    z = num3
    return min(x, y, z)





# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    x = number
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

    





# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    i = 1
    result = ""
    while i <= rows:
        result += "*" * (i) +"\n"
        i += 1
    return result.rstrip()
    







# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ""
    for i in range(1):
        for j in range(1, limit+1):
            if j % 3 == 0:
                result += "Multiple of 3" + "\n"
            else:
                result += str(j) + "\n"
    return result.rstrip()
    
print(count_multiples_of_3(7))    

    


    





# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(x, y):
    i = 1
    result = 0
    for i in range(x, y+1):
        if i % 2 == 0:
                result += i
    return result
    




