import doctest
import math

def exponentiation(x: int, y: int) -> int:
    """
    Exponentiation is an arithmetic operation used as a result of multiple multiplication by itself.
    :param x: base
    :param y: index
    :return: result exaltation
    >>> exponentiation(3, 3)
    27
    """
    return x ** y


if __name__ == '__main__':
    doctest.testmod()



def sqrt(x: int) -> int:
    """
    The arithmetic square root of a non-negative number a is a non-negative number whose square is equal to a.
    :param x: non-negative number
    :return: umber whose square is equal to a
    >>> sqrt(9)
    3.0

    """
    return math.sqrt(x)

if __name__ == '__main__':
       doctest.testmod()


def percentage(x: int, y: int) -> int:
     """
     Percentage is one hundredth of any number. The designator is%.
     :param x: Number
     :param y: Percent%
     :return: Percentage of number
     >>> percentage(10, 8)
     0.8
     """
     return x / 100 * y

if __name__ == '__main__':
       doctest.testmod()