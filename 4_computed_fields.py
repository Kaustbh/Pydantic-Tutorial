from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float # kg
    height: float # mtr
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    married : bool = None

    @computed_field
    @property
    def bmi(self) -> float:
        cal_bmi = self.weight / (self.height ** 2)
        return round(cal_bmi, 2)


def insert_patient(patient: Patient):

    print(f"Inserting patient: {patient.name}, Age: {patient.age}")

    print(type(patient.age))
    print(f"BMI: {patient.bmi}") # you should give the method name

details = {'name': 'Nitish', 'email': 'abc@hdfc.com','linkedin_url': 'htt://www.linkedin.com', 'age': 50, 'weight': 70, 'height': 1.8, 'allergies': ['pollen','dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '1234567890'}}

patient1 = Patient(**details)
insert_patient(patient1)