# Dijkstra
import types
from types import GeneratorType


# Napisz funkcje, do dodawania liczb


def add(a):
    result = 0
    for i in range(a + 1):
        result += i
    return result


print(add(10))


def add2(a):
    result = 0
    while a > 0:
        result += a
        a -= 1
    return result


print(add2(100))

# recursion

import sys


def add3(n):
    if n == 0:
        return n
    else:
        return n + add3(n - 1)


print(add3(100))

print(sys.getrecursionlimit())


# sys.setrecursionlimit(10000)

# def add4(n, acc=0):
#     if n == 0:
#         return n
#     else:
#         return n + add4(n - 1, acc + n)
#
# print(add4(1000))


# Alex Bill

def tramp(gen, *arg, **kwargs):
    g = gen(*arg, **kwargs)

    while isinstance(g, types.GeneratorType):
        g = next(g)

    return g


# recursion
# big O: 2 ** n
def f(a):
    if a <= 1:
        return a
    else:
        return f(a - 1) + f(a - 2)


# iteration
def f1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def ft(n, curr=0, next_=1):
    if n == 0:
        yield curr
    else:
        yield ft(n - 1, next_, curr + next_)


# import sys
#
# sys.set_int_max_str_digits(20899)
# print(tramp(ft, 100_000))


# napisz fn do usuwania zanków
# 'ala ma kota!?' -> !? -> ala ma kota
# bez regex
# uzyj rekurencji (replace)

def recur_swap(text):
    if '!?' in text:
        return recur_swap(text.replace('!?', ''))
    else:
        return text

print(recur_swap('ala ma kota!?'))


def recur_swap2(text: str, chars: str) -> str:
    if chars:
        return recur_swap2(text.replace(chars[0], ""),chars[1:] )
    return text


print(recur_swap2('ala ma kota!?', '!?'))