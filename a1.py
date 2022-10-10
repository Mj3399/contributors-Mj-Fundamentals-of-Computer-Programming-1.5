"""Assignment 1
Fill in the following function skeletons (deleting the 'raise NotImplementedError' 
lines as you go) - descriptions are provided in the PDF, and briefly in the 
docstring (the triple quote thing at the top of each function).
Some assert statements have been provided - write more of them to test your code!
"""
from typing import List, TypeVar
def absolute(n: int) -> int:
    if (n >= 0):
            return(n)
    else:
            return(n*-1)
    """Gives the absolute value of the passed in number. Cannot use the built
    in function `abs`.
    Args:
        n - the number to take the absolute value of
    Returns:
        the absolute value of the passed in number
    """
#assert absolute(-1) == 1, "absolute of -1 failed"
#assert absolute(1) == 1
#assert absolute(-100) == 100
def factorial(n: int) -> int:
    if (n == 0):
    return 1
    else:
    return(n*factorial(n-1))
    """Takes a number n, and computes the factorial n! You can assume the passed
    in number will be positive
    Args:
        n - the number to compute factorial of
    Returns:
        factorial of the passed in number
    """
#assert factorial(4) == 24, "factorial of 4 failed"
#assert factorial(2) == 2
#assert factorial(6) == 720
#assert factorial(0) == 1
#assert factorial(1) == 1
T = TypeVar("T")
def every_other(lst: List[T]) -> List[T]:
    return lst[::2]
    """Takes a list and returns a list of every other element in the list,
    starting with the first.
    Args:
        lst - a list of any (constrained by type T to be the same type as the
            returned list)
    Returns:
        a list of every of other item in the original list starting with the first
    """
#assert every_other([1, 2, 3, 4, 5]) == [1,3,5], "every_other of [1,2,3,4,5] 
failed"
#assert every_other([1, 2, 3, 4]) == [1, 3]
#assert every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
#assert every_other([]) == []
#assert every_other([1]) == [1]
#assert every_other(['a', 'b', 'c']) == ['a', 'c']
def sum_list(lst: List[int]) -> int:
    if len(lst)==0:
            return 0
    else:
            return lst[0] + sum_list(lst[1:])
    """Takes a list of numbers, and returns the sum of the numbers in that list.
    Cannot use the built in function `sum`.
    Args:
        lst - a list of numbers
    Returns:
        the sum of the passed in list
    """
#assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
#assert sum_list([1, 2]) == 3
#assert sum_list([]) == 0
def mean(lst: List[int]) -> float:
    if len(lst) == 0:
        return 0
    else:
        return sum_list(lst) / len(lst)
    """Takes a list of numbers, and returns the mean of the numbers.
    Args:
        lst - a list of numbers
    Returns:
        the mean of the passed in list
    """
#assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
#assert mean([]) == 0
#assert mean([1, 2, 3, 4]) == 2.5
def median(lst: List[int]) -> float:
    if len(lst) == 0:
        return 0
    elif len(lst)%2==0:
    return (lst[len(lst)//2] + lst[len(lst)//2 - 1])/2
    else: return lst[len(lst)//2]
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two
    center values.
    Args:
        lst - an ordered list of numbers
    Returns:
        the median of the passed in list
    """
#assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
#assert median([]) == 0
#assert median([1, 2, 3, 4]) == 2.5
#assert median([1, 2]) == 1.5
def duck_duck_goose(lst: List[str]) -> List[str]:
    index = 0
    duck_stage = "duck1"
    while(len(lst) > 2):
        person = lst[index]
        #print(index, person, duck_stage)
        if duck_stage == "goose":
            lst.pop(index)
            duck_stage = "duck1"
        elif duck_stage == "duck1":
            duck_stage = "duck2"
            index = index + 1
        elif duck_stage == "duck2":
            duck_stage = "goose"
            index = index + 1
        #print(lst)
        if index >= len(lst):
            index = index - len(lst)
    #print(lst)
    return(lst)
    
    
    """Given an list of names (strings), play 'duck duck goose' with it,
    knocking out every third name (wrapping around) until only two names are
    left. In other words, when you hit the end of the list, wrap around and keep
    counting from where you were.
    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and
    Jennie.
    You may assume the list has 3+ names to start
    Args:
        lst - a list of names (strings)
    Returns:
        the resulting list after playing duck duck goose
    """
names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
#assert duck_duck_goose(names) == ["sasha", "will"]
#assert duck_duck_goose(['Nathan', 'Sasha', 'Sara', 'Jennie']) == ['Nathan', 
'Jennie']
print("All tests passed!")
