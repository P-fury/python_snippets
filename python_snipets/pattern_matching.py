# simple match
from collections.abc import Callable


def ex_1():
    while True:
        command = input('Enter command: \n')
        match command:
            case "add todo":
                print(f"ToDo added!")
            case "show todos":
                print('yours todos')
            case "bye":
                print('bye bye !')
                break

            case _:
                print("unknown command")


# match on different types
def ex_2():
    for x in 1, 'two', 3.14, Exception('yolo'), lambda data: data + 42, [1, 2, 3], (1, 2, 3):
        match x:
            case int():
                print(f"int: {x}")
            case str():
                print(f"str: {x}")
            case float():
                print(f"float: {x}")
            case Exception():
                print(f"Exception: {x}")
            case Callable():
                print(f"callable: {x}")
            case y:
                print(f"unknown: {y}")


# guarded matching
def ex_3():
    for i in range(6):
        match i:
            case 1 | 3 | 5 if i < 4:
                print(f"{i} is odd and less then 4")
            case 1 | 3 | 5 if i > 4:
                print(f"{i} is odd and greater than 4")
            case 2 | 4:
                print(f"{i} is even")


def ex_4():
    for calls in [1,2,3], (4,5,6,7,6,5,3,4,5), {"a":42}:
        match calls:
            case [1,2,3] as my_list:
                print(f"list: {my_list}")
            case (_,5 as my_int, _, *i) as my_tupe:
                print(f"tuple: {my_tupe} with {my_int}")
            case {"a": 42} as my_dict:
                print(f"dict: {my_dict}")
            case _:
                print(f"unknown: {calls}")



# walrus operator (dynamiczne tworzenie zmiennej)
def ex_5():
    match the_answer:= 2* 1* 3*7:
        case _:
            print(f'the answer is {the_answer}')

ex_5()