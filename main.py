from typing import NamedTuple, Dict, NewType
from collections import namedtuple


'''
class OldModel:
    def __init__(self, user_id, user_name, permissions):
        user_id = int(user_id)
        user_name = int(user_name)
        permissions = permissions

privileges = {"Read": True, "Write": True, "Create": True, "Edit": True, "Delete": True}
User = OldModel(1, "admin", privileges)
'''

#=======================================================================================================================


Permissions = namedtuple('Permissions', ["Read", "Write", "Create", "Edit", "Delete"]) # Обращение объекту через точку, т.е. Permissions.Read или Permissions.Write
'''
Зачем это нужно? Например:
for user in users:
    if user.permissions.Edit == True: #можно просто 'if user.permissions.Write'
        print(f"Пользователь {user.user_name} может редактировать статью")
        
'''
UserId = NewType("UserId", int) # Создание своего типа данных на основе примитивов (в данном случае примитив это int)
UserName = NewType("UserName", str)

# Автоматическая проверка на то, что аргументы функции соответствуют нужному типу (проверка на ошибки)
# Знак "->" указывает на тип возвращаемого значения функции
def NewModel(user_id: UserId, user_name: UserName, permissions: NamedTuple) -> NamedTuple:
    permissions: Dict[str, bool] = {'read': permissions.Read, 'write': permissions.Write, 'create': permissions.Create, 'edit': permissions.Edit, 'delete': permissions.Delete}
    properties = NamedTuple('properties', [("user_id", int), ("user_name", str), ("permissions", NamedTuple)])
    properties.user_name = user_name
    properties.user_id = user_id
    properties.permissions = permissions
    return properties

admin = NewModel(UserId(1), UserName("admin"), Permissions(True, True, True, True, True))

print(admin.user_id)
