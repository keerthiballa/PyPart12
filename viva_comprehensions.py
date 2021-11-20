from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    Answer: This function is to return the list of odd or even parity between start and stop integers

    :param start: start integer (inclusive)
    :param stop: stop integer (exclusive)
    :param parity: Parity.ODD or Parity.EVEN
    :return: List of integers of indicated Parity between start and stop (exclusive) integers indicated
    """
    if parity is Parity.ODD: #odd
        output = [a for a in range(start, stop) if a%2 == 1]

    else: #even
        output = [a for a in range(start, stop) if a%2 == 0]

    return output


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    Answer: This function is to return the dictionary of x as keys and strategy(x) as values between start and stop integers

    :param start:start integer (inclusive)
    :param stop:stop integer (exclusive)
    :param strategy: strategy is callable to which the iterator is passed on
    :return: dictionary of x as keys and strategy(x) as values
    """
    output = {x: strategy(x) for x in range(start, stop)}
    return output


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    Answer: This function is to return the set (in ascending order) of lower case characters in a given string after converting them to upper case characters

    :param val_in: input string
    :return:
    """
    output = {val_in[x].upper() for x in range(0,len(val_in)) if val_in[x].islower()}
    list(output).sort()
    return set(output)
