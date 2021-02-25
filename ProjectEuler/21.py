"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
def amicable_number(x):
    amic_range = range(1, x)
    amicable_numbers = []

    for num in amic_range:

        x_val = 0
        y_val = 0
        first_iter_list = range(1, num)
        for val in first_iter_list:
            if (num%val)==0:
                x_val+=val

        for val in range(1, x_val):
            if (x_val%val)==0:
                y_val+=val

        if y_val==num:
            amicable_numbers.append(y_val)

    result = sum(amicable_numbers)

    return result

amicable_num_result = amicable_number(10000)

