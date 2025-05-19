from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int
    city:str
new_person:Person={'name':'John Doe','age':30,'city':'New York'}
print(new_person)