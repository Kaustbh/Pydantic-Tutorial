from pydantic import BaseModel


class Adderess(BaseModel):

    city:str
    state:str
    pin:str
class Patient(BaseModel):

    name:str
    age: int
    gender:str
    adderess: Adderess

adderess_dict = {'city':'gurgoan', 'state':'haryana', 'pin':'122001'}

address_1 = Adderess(**adderess_dict)

name_dict = {'name':'Nitish', 'age':30, 'gender':'male', 'adderess': address_1}
patient1 = Patient(**name_dict)

print(patient1)
print(patient1.adderess.state)