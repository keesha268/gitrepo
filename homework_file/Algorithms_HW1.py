# QUESTION 1

def sum_of_digits(n: int):
    final_result = 0
    for i in range(n + 1):
        final_result = final_result + i
    return final_result

test = 5
result = sum_of_digits(test)
print(result)



# QUESTION 2

def max_number(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c


result = max_number(25, 50, 75)
print(result)



# QUESTION 3

def odd_and_even_digits(n):
    odd = 0
    even = 0

    while n != 0:
        digit = n % 10
        if digit % 2:
            odd += 1
        else:
            even += 1
        n = n // 10


    print(f"Odd digits: {odd}")
    print(f"Even digits: {even}")

test = 87256
odd_and_even_digits(test)


