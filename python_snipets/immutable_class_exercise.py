from dataclasses import dataclass, asdict
import dataclasses
from typing import Generator


@dataclass(frozen=True)
class Todo:
    name: str
    status: str = 'pending'


@dataclass(frozen=True)
class TodoList:
    todos: tuple[Todo, ...]


t1 = Todo('Python')
t2 = Todo('Data Science')
t3 = Todo('MLOPS')

t_coll = TodoList((t1, t2, t3))

print(t_coll)


# CHANING NAME IN TO DO LIST

# def change_name(todos_tuple: TodoList, old_item: str, new_item: str) -> TodoList:
#     index = next((i for i, todo in enumerate(todos_tuple.todos) if todo.name == old_item), None)
#     if index is None:
#         print(f'{old_item} doesn\'t exist')
#         return todos_tuple
#
#     updated_todos = (
#             todos_tuple.todos[:index]
#             + (Todo(new_item),)
#             + todos_tuple.todos[index + 1:]
#     )
#     return TodoList(updated_todos)
#
#
# print(change_name(t_coll, 'MLOPS', 'Bajton'))
#
# print(t1)


def change_todo_name(todo: Todo, name: str) -> Todo:
    return dataclasses.replace(todo, name=name)
    # return Todo(**(asdict(todo)) | {"name":name})


def update_todos(todo_list: TodoList, prev_todo: Todo, next_todo: Todo) -> TodoList:
    def replace_todo(todo: Todo) -> Todo:
        if todo is not prev_todo:
            return todo
        return next_todo

    return TodoList(tuple(map(replace_todo, todo_list.todos)))


tx = change_todo_name(t1, 'yolo')
t_coll = update_todos(t_coll, t1, tx)
print(t_coll)



# EXAMPLE CURRING:

def add(a,b):
    return a+b

def curry(a):
    def _(b):
        return a + b
    return _

print(curry(1)(2))


def sub(a,b):
    return a-b


def curry2(fn):
    def _(a):
        def __(b):
            return fn(a,b)
        return __
    return _

print(curry2(sub)(1)(2))
print(curry2(add)(1)(2))


