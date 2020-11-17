from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Function returns a list of either ODD or EVEN integers depending on the
    parity argument. List will begin at 'start' argument and end at 'stop'
    argument ('stop' exclusive).

    :param start: int representing value to start list
    :param stop: int representing value to end list (exclusive)
    :param parity: parity object that determines whether to return ODD or EVEN ints
    :return: list of either ODD or EVEN ints
    """
    if parity.name == 'ODD':
        return [x for x in range(start, stop) if x % 2 != 0]
    elif parity.name == 'EVEN':
        return [x for x in range(start, stop) if x % 2 == 0]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Function returns a dict where keys are ints from 'start' argument
    to stop argument (exclusive) and values are the result of each key
    after being passed to strategy argument.

    :param start: int representing value to start dict keys
    :param stop: int representing value to end dict keys (exclusive)
    :param strategy: function to be run on each individual key of dict
    :return: dict where keys are ints from 'start' argument
    to stop argument (exclusive) and values are the result of each key
    after being passed to strategy argument.
    """
    return {x: strategy(x) for x in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    Function returns a set of lowercase chars in the str 'val_in' argument.
    Will return chars as uppercase.

    :param val_in: str to iterate over
    :return: set of lowercase chars in str 'val_in' argument. Will return
    chars as uppercase
    """
    return {x.upper() for x in val_in if x.islower()}
