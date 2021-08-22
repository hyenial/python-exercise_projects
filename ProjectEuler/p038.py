'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''

from lib.digital import num_digits, is_pandigital


def concatenated_product(a: int, n: int) -> int:
    """ Build the concatenated product :math:`a` and :math:`(1, 2, \\dots, n)`

    The concatenated product of :math:`a` and :math:`(1, 2, \\dots, n)` is defined as
    :math:`(1 \\times a) || (2 \\times a) || \\dots || (n \\times a)`

    :param a: the base integer
    :param n: the number of products in the concatenated product
    :return: the concatenated product of :math:`a` and :math:`(1, 2, \\dots, n)`
    """

    vals = [i * a for i in range(1, n + 1)]
    z = 0
    for val in vals:
        z = z * (10 ** num_digits(val)) + val

    return z


def solve():
    """ Compute the answer to Project Euler's problem #38 """

    answer = 918273645  # we are searching for a greater answer, this will do as a starting value to maximise

    # The range of the search space on a for each possible value of n
    bounds = {2: (1234, 10 ** 4), 3: (123, 10 ** 3), 4: (12, 10 ** 2), 5: (1, 10 ** 1), 6: (1, 10 ** 1),
              7: (1, 10 ** 1), 8: (1, 10 ** 1), 9: (1, 10 ** 1)}

    # Perform the search
    for n in range(2, 10):
        for a in range(*bounds[n]):
            concat_prod = concatenated_product(a, n)
            if is_pandigital(concat_prod, 9):
                answer = max(answer, concat_prod)

    return answer
